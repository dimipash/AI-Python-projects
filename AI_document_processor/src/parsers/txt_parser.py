
"""
Plain text document parser.
Handles text extraction and metadata for .txt files.
"""

import os
from datetime import datetime
import logging

from .base import BaseDocumentParser, DocumentParserError
from ..models import Document, DocumentMetadata, DocumentType

logger = logging.getLogger(__name__)


class TxtParser(BaseDocumentParser):
    """Plain text document parser for .txt files."""

    def __init__(self):
        """Initialize the TxtParser."""
        super().__init__()
        self.supported_types = [DocumentType.TXT]
        self.logger = logging.getLogger(self.__class__.__name__)

    def can_parse(self, file_path: str) -> bool:
        """
        Check if this parser can handle the given file.

        Args:
            file_path: Path to the file to check.

        Returns:
            True if the file is a .txt file, False otherwise.
        """
        try:
            # Check file extension
            _, ext = os.path.splitext(file_path.lower())
            if ext != ".txt":
                return False

            # Validate file
            self.validate_file(file_path)

            return True
        except Exception as e:
            self.logger.warning(f"Cannot parse TXT {file_path}: {e}")
            return False

    def parse(self, file_path: str, **kwargs) -> Document:
        """
        Parse the text document and return a Document object.

        Args:
            file_path: Path to the text file.
            **kwargs: Additional parsing options (e.g., encoding).

        Returns:
            Document object with extracted content and metadata.

        Raises:
            DocumentParserError: If parsing fails.
        """
        try:
            self.log_parsing_progress(f"Starting TXT parsing: {file_path}")

            # Extract metadata first
            metadata = self.extract_metadata(file_path)

            # Extract text content
            content = self.extract_text(file_path, **kwargs)

            # Create document object
            document = self.create_document(file_path, content, metadata)

            self.log_parsing_progress(f"Successfully parsed TXT: {file_path}")

            return document

        except Exception as e:
            error_msg = f"Failed to parse TXT {file_path}: {str(e)}"
            self.log_parsing_progress(error_msg, "error")
            raise DocumentParserError(error_msg) from e

    def extract_text(self, file_path: str, **kwargs) -> str:
        """
        Extract text content from the text document.

        Args:
            file_path: Path to the text file.
            **kwargs: Additional extraction options (e.g., encoding).

        Returns:
            Extracted text content.

        Raises:
            DocumentParserError: If text extraction fails.
        """
        try:
            encoding = kwargs.get("encoding", "utf-8")
            with open(file_path, "r", encoding=encoding) as f:
                text = f.read()
            return self.clean_text(text)
        except Exception as e:
            raise DocumentParserError(
                f"Failed to extract text from TXT: {str(e)}"
            ) from e

    def extract_metadata(self, file_path: str) -> DocumentMetadata:
        """
        Extract metadata from the text document.

        Args:
            file_path: Path to the text file.

        Returns:
            DocumentMetadata object with extracted metadata.

        Raises:
            DocumentParserError: If metadata extraction fails.
        """
        try:
            metadata = DocumentMetadata()
            file_info = self.get_file_info(file_path)

            metadata.file_size = file_info["size"]
            metadata.creation_date = datetime.fromtimestamp(file_info["created"])
            metadata.modification_date = datetime.fromtimestamp(file_info["modified"])

            return metadata
        except Exception as e:
            raise DocumentParserError(
                f"Failed to extract TXT metadata: {str(e)}"
            ) from e
