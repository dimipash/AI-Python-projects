"""
PDF document parser using PyMuPDF (fitz).
Handles text extraction, metadata extraction, and image processing from PDF files.
"""

import os
import io
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
import logging
from datetime import datetime

try:
    import fitz  # PyMuPDF
except ImportError:
    raise ImportError(
        "PyMuPDF is required for PDF parsing. Install with: pip install PyMuPDF"
    )

from PIL import Image
import mimetypes

from .base import BaseDocumentParser, DocumentParserError
from ..models import Document, DocumentMetadata, DocumentType
from ..config import settings

logger = logging.getLogger(__name__)


class PDFParser(BaseDocumentParser):
    """PDF document parser using PyMuPDF."""

    def __init__(self):
        """Initialize the PDF parser."""
        super().__init__()
        self.supported_types = [DocumentType.PDF]
        self.logger = logging.getLogger(self.__class__.__name__)

    def can_parse(self, file_path: str) -> bool:
        """
        Check if this parser can handle the given PDF file.

        Args:
            file_path: Path to the file to check

        Returns:
            True if the file is a valid PDF, False otherwise
        """
        try:
            # Check file extension
            _, ext = os.path.splitext(file_path.lower())
            if ext != ".pdf":
                return False

            # Validate file
            self.validate_file(file_path)

            # Try to open the PDF with PyMuPDF
            doc = fitz.open(file_path)
            is_pdf = doc.is_pdf
            doc.close()

            return is_pdf
        except Exception as e:
            self.logger.warning(f"Cannot parse PDF {file_path}: {e}")
            return False

    def parse(self, file_path: str, **kwargs) -> Document:
        """
        Parse the PDF document and return a Document object.

        Args:
            file_path: Path to the PDF file
            **kwargs: Additional parsing options:
                - extract_images: bool (default False)
                - preserve_layout: bool (default True)
                - password: str (optional PDF password)

        Returns:
            Document object with extracted content and metadata

        Raises:
            DocumentParserError: If parsing fails
        """
        try:
            self.log_parsing_progress(f"Starting PDF parsing: {file_path}")

            # Extract metadata first
            metadata = self.extract_metadata(file_path)

            # Extract text content
            content = self.extract_text(file_path, **kwargs)

            # Create document object
            document = self.create_document(file_path, content, metadata)

            # Extract images if requested
            extract_images = kwargs.get("extract_images", False)
            if extract_images:
                images = self.extract_images(file_path)
                document.metadata.keywords.extend([f"image_count_{len(images)}"])

            self.log_parsing_progress(f"Successfully parsed PDF: {file_path}")

            return document

        except Exception as e:
            error_msg = f"Failed to parse PDF {file_path}: {str(e)}"
            self.log_parsing_progress(error_msg, "error")
            raise DocumentParserError(error_msg) from e

    def extract_text(self, file_path: str, **kwargs) -> str:
        """
        Extract text content from the PDF document.

        Args:
            file_path: Path to the PDF file
            **kwargs: Additional extraction options
                - preserve_layout: bool (default True)
                - password: str (optional PDF password)

        Returns:
            Extracted text content

        Raises:
            DocumentParserError: If text extraction fails
        """
        try:
            preserve_layout = kwargs.get("preserve_layout", True)
            password = kwargs.get("password", None)

            text_parts = []

            with fitz.open(file_path) as doc:
                # Check if PDF is password protected
                if doc.needs_pass and not password:
                    raise DocumentParserError("PDF requires password but none provided")

                # Authenticate with password if needed
                if doc.needs_pass and password:
                    if not doc.authenticate(password):
                        raise DocumentParserError("Invalid PDF password")

                # Extract text from each page
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)

                    if preserve_layout:
                        # Extract text with layout preservation
                        text = page.get_text("text")
                    else:
                        # Extract text blocks
                        text = page.get_text("blocks")
                        text = "\n".join(block[4] for block in text if block[4].strip())

                    if text.strip():
                        text_parts.append(f"\n--- Page {page_num + 1} ---\n{text}")

            full_text = "\n".join(text_parts)
            return self.clean_text(full_text)

        except Exception as e:
            raise DocumentParserError(
                f"Failed to extract text from PDF: {str(e)}"
            ) from e

    def extract_metadata(self, file_path: str) -> DocumentMetadata:
        """
        Extract metadata from the PDF document.

        Args:
            file_path: Path to the PDF file

        Returns:
            DocumentMetadata object with extracted metadata

        Raises:
            DocumentParserError: If metadata extraction fails
        """
        try:
            with fitz.open(file_path) as doc:
                metadata = DocumentMetadata()

                # Extract PDF metadata
                pdf_metadata = doc.metadata

                # Map PDF metadata to our DocumentMetadata fields
                metadata.title = pdf_metadata.get("title")
                metadata.author = pdf_metadata.get("author")
                metadata.subject = pdf_metadata.get("subject")
                metadata.creator = pdf_metadata.get("creator")
                metadata.producer = pdf_metadata.get("producer")

                # Handle dates
                creation_date = pdf_metadata.get("creationDate")
                if creation_date:
                    try:
                        # PDF dates are in format: D:YYYYMMDDHHmmSSOHH'mm'
                        metadata.creation_date = self._parse_pdf_date(creation_date)
                    except Exception:
                        pass

                mod_date = pdf_metadata.get("modDate")
                if mod_date:
                    try:
                        metadata.modification_date = self._parse_pdf_date(mod_date)
                    except Exception:
                        pass

                # Set page count
                metadata.page_count = len(doc)

                # Extract keywords
                keywords = pdf_metadata.get("keywords")
                if keywords:
                    metadata.keywords = [kw.strip() for kw in keywords.split(",")]

                # Calculate file size
                path = Path(file_path)
                metadata.file_size = path.stat().st_size

                return metadata

        except Exception as e:
            raise DocumentParserError(
                f"Failed to extract PDF metadata: {str(e)}"
            ) from e

    def extract_images(
        self, file_path: str, output_dir: Optional[str] = None
    ) -> List[str]:
        """
        Extract images from the PDF document.

        Args:
            file_path: Path to the PDF file
            output_dir: Directory to save extracted images (optional)

        Returns:
            List of extracted image data or file paths
        """
        try:
            images = []

            with fitz.open(file_path) as doc:
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    image_list = page.get_images()

                    for img_index, img in enumerate(image_list):
                        # Get image data
                        xref = img[0]
                        pix = fitz.Pixmap(doc, xref)

                        # Skip CMYK images (not supported by PIL)
                        if pix.n - pix.alpha < 4:
                            img_data = pix.tobytes("png")

                            if output_dir:
                                # Save to file
                                os.makedirs(output_dir, exist_ok=True)
                                img_filename = (
                                    f"page_{page_num + 1}_img_{img_index + 1}.png"
                                )
                                img_path = os.path.join(output_dir, img_filename)

                                with open(img_path, "wb") as f:
                                    f.write(img_data)
                                images.append(img_path)
                            else:
                                # Return as bytes
                                images.append(img_data)

                        pix = None  # Free memory

            return images

        except Exception as e:
            self.logger.warning(f"Failed to extract images from PDF: {e}")
            return []

    def is_scanned_pdf(self, file_path: str) -> bool:
        """
        Check if the PDF is likely scanned (image-based) by analyzing text content.

        Args:
            file_path: Path to the PDF file

        Returns:
            True if the PDF appears to be scanned, False otherwise
        """
        try:
            with fitz.open(file_path) as doc:
                total_chars = 0
                total_pages = len(doc)

                for page in doc:
                    text = page.get_text()
                    total_chars += len(text.strip())

                # If average characters per page is very low, likely scanned
                avg_chars_per_page = total_chars / total_pages if total_pages > 0 else 0

                # Threshold can be adjusted
                is_scanned = avg_chars_per_page < 50

                self.logger.info(
                    f"PDF scanning check: avg_chars_per_page={avg_chars_per_page:.1f}, is_scanned={is_scanned}"
                )
                return is_scanned

        except Exception as e:
            self.logger.warning(f"Failed to check if PDF is scanned: {e}")
            return False

    def _parse_pdf_date(self, date_str: str) -> Optional[datetime]:
        """
        Parse PDF date string to datetime object.

        Args:
            date_str: PDF date string in format D:YYYYMMDDHHmmSSOHH'mm'

        Returns:
            datetime object or None if parsing fails
        """
        try:
            # Remove "D:" prefix if present
            if date_str.startswith("D:"):
                date_str = date_str[2:]

            # Extract date components
            year = int(date_str[0:4])
            month = int(date_str[4:6])
            day = int(date_str[6:8])

            # Extract time components (if present)
            hour = int(date_str[8:10]) if len(date_str) > 8 else 0
            minute = int(date_str[10:12]) if len(date_str) > 10 else 0
            second = int(date_str[12:14]) if len(date_str) > 12 else 0

            return datetime(year, month, day, hour, minute, second)

        except Exception:
            return None

    def get_pdf_info(self, file_path: str) -> Dict[str, Any]:
        """
        Get detailed information about the PDF file.

        Args:
            file_path: Path to the PDF file

        Returns:
            Dictionary with PDF information
        """
        try:
            with fitz.open(file_path) as doc:
                info = {
                    "page_count": len(doc),
                    "is_pdf": doc.is_pdf,
                    "needs_password": doc.needs_pass,
                    "is_encrypted": doc.is_encrypted,
                    "permissions": doc.permissions,
                    "has_images": False,
                    "estimated_words": 0,
                    "is_scanned": False,
                }

                # Check for images
                for page in doc:
                    if page.get_images():
                        info["has_images"] = True
                        break

                # Estimate word count
                total_text = ""
                for page in doc:
                    total_text += page.get_text()

                info["estimated_words"] = len(total_text.split())

                # Check if scanned
                info["is_scanned"] = self.is_scanned_pdf(file_path)

                return info

        except Exception as e:
            raise DocumentParserError(f"Failed to get PDF info: {str(e)}") from e
