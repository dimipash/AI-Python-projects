"""
Base document parser interface and common utilities.
Defines the abstract interface that all document parsers must implement.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, BinaryIO
from pathlib import Path
import logging
import mimetypes
import os

from ..models import Document, DocumentType, DocumentMetadata
from ..config import settings

logger = logging.getLogger(__name__)


class DocumentParserError(Exception):
    """Exception raised when document parsing fails."""

    pass


class BaseDocumentParser(ABC):
    """Abstract base class for document parsers."""

    def __init__(self):
        """Initialize the parser."""
        self.supported_types = []
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def can_parse(self, file_path: str) -> bool:
        """
        Check if this parser can handle the given file.

        Args:
            file_path: Path to the file to check

        Returns:
            True if the parser can handle the file, False otherwise
        """
        pass

    @abstractmethod
    def parse(self, file_path: str, **kwargs) -> Document:
        """
        Parse the document and return a Document object.

        Args:
            file_path: Path to the file to parse
            **kwargs: Additional parsing options

        Returns:
            Document object with extracted content and metadata

        Raises:
            DocumentParserError: If parsing fails
        """
        pass

    @abstractmethod
    def extract_text(self, file_path: str) -> str:
        """
        Extract text content from the document.

        Args:
            file_path: Path to the file

        Returns:
            Extracted text content
        """
        pass

    @abstractmethod
    def extract_metadata(self, file_path: str) -> DocumentMetadata:
        """
        Extract metadata from the document.

        Args:
            file_path: Path to the file

        Returns:
            DocumentMetadata object
        """
        pass

    def get_document_type(self, file_path: str) -> DocumentType:
        """
        Determine the document type from file extension and MIME type.

        Args:
            file_path: Path to the file

        Returns:
            DocumentType enum value
        """
        # Get file extension
        _, ext = os.path.splitext(file_path.lower())

        # Get MIME type
        mime_type, _ = mimetypes.guess_type(file_path)

        # Map extensions to document types
        type_mapping = {
            ".pdf": DocumentType.PDF,
            ".docx": DocumentType.DOCX,
            ".doc": DocumentType.DOCX,
            ".txt": DocumentType.TXT,
            ".text": DocumentType.TXT,
            ".png": DocumentType.IMAGE,
            ".jpg": DocumentType.IMAGE,
            ".jpeg": DocumentType.IMAGE,
            ".tiff": DocumentType.IMAGE,
            ".tif": DocumentType.IMAGE,
            ".bmp": DocumentType.IMAGE,
            ".gif": DocumentType.IMAGE,
        }

        # Map MIME types to document types
        mime_mapping = {
            "application/pdf": DocumentType.PDF,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": DocumentType.DOCX,
            "application/msword": DocumentType.DOCX,
            "text/plain": DocumentType.TXT,
            "text/rtf": DocumentType.TXT,
            "image/png": DocumentType.IMAGE,
            "image/jpeg": DocumentType.IMAGE,
            "image/tiff": DocumentType.IMAGE,
            "image/bmp": DocumentType.IMAGE,
            "image/gif": DocumentType.IMAGE,
        }

        # Try extension first
        doc_type = type_mapping.get(ext)

        # Fallback to MIME type
        if not doc_type and mime_type:
            doc_type = mime_mapping.get(mime_type)

        return doc_type or DocumentType.UNKNOWN

    def validate_file(self, file_path: str) -> bool:
        """
        Validate that the file exists and is accessible.

        Args:
            file_path: Path to the file

        Returns:
            True if valid, raises DocumentParserError if invalid
        """
        path = Path(file_path)

        if not path.exists():
            raise DocumentParserError(f"File does not exist: {file_path}")

        if not path.is_file():
            raise DocumentParserError(f"Path is not a file: {file_path}")

        if not os.access(file_path, os.R_OK):
            raise DocumentParserError(f"File is not readable: {file_path}")

        # Check file size
        file_size = path.stat().st_size
        max_size = settings.max_file_size_mb * 1024 * 1024

        if file_size > max_size:
            raise DocumentParserError(
                f"File size ({file_size} bytes) exceeds maximum allowed size ({max_size} bytes)"
            )

        return True

    def get_file_info(self, file_path: str) -> Dict[str, Any]:
        """
        Get basic file information.

        Args:
            file_path: Path to the file

        Returns:
            Dictionary with file information
        """
        path = Path(file_path)
        stat = path.stat()

        return {
            "name": path.name,
            "size": stat.st_size,
            "created": stat.st_ctime,
            "modified": stat.st_mtime,
            "extension": path.suffix.lower(),
            "mime_type": mimetypes.guess_type(file_path)[0],
        }

    def create_document(
        self, file_path: str, content: str, metadata: Optional[DocumentMetadata] = None
    ) -> Document:
        """
        Create a Document object from extracted content and metadata.

        Args:
            file_path: Original file path
            content: Extracted text content
            metadata: Document metadata

        Returns:
            Document object
        """
        from ..models import ProcessingOptions

        if metadata is None:
            metadata = DocumentMetadata()

        # Ensure file_size is set
        if metadata.file_size is None:
            path = Path(file_path)
            metadata.file_size = path.stat().st_size

        document = Document(
            filename=os.path.basename(file_path),
            file_path=file_path,
            file_type=self.get_document_type(file_path),
            file_size=metadata.file_size,
            content=content,
            metadata=metadata,
            processing_options=ProcessingOptions(),
        )

        return document

    def clean_text(self, text: str) -> str:
        """
        Clean and normalize extracted text.

        Args:
            text: Raw extracted text

        Returns:
            Cleaned text
        """
        if not text:
            return ""

        # Remove excessive whitespace
        text = " ".join(text.split())

        # Remove control characters except newlines and tabs
        text = "".join(char for char in text if ord(char) >= 32 or char in "\n\t")

        return text.strip()

    def log_parsing_progress(self, message: str, level: str = "info"):
        """
        Log parsing progress.

        Args:
            message: Log message
            level: Log level (info, warning, error)
        """
        log_method = getattr(self.logger, level, self.logger.info)
        log_method(message)


class ParserRegistry:
    """Registry for document parsers."""

    def __init__(self):
        """Initialize the parser registry."""
        self._parsers: List[BaseDocumentParser] = []
        self.logger = logging.getLogger(self.__class__.__name__)

    def register(self, parser: BaseDocumentParser):
        """
        Register a document parser.

        Args:
            parser: Parser instance to register
        """
        self._parsers.append(parser)
        self.logger.info(f"Registered parser: {parser.__class__.__name__}")

    def get_parser(self, file_path: str) -> Optional[BaseDocumentParser]:
        """
        Get the appropriate parser for a file.

        Args:
            file_path: Path to the file

        Returns:
            Parser instance or None if no suitable parser found
        """
        for parser in self._parsers:
            try:
                if parser.can_parse(file_path):
                    return parser
            except Exception as e:
                self.logger.warning(
                    f"Parser {parser.__class__.__name__} failed to check file {file_path}: {e}"
                )

        return None

    def list_parsers(self) -> List[str]:
        """
        List all registered parsers.

        Returns:
            List of parser class names
        """
        return [parser.__class__.__name__ for parser in self._parsers]

    def clear(self):
        """Clear all registered parsers."""
        self._parsers.clear()


# Global parser registry instance
parser_registry = ParserRegistry()
