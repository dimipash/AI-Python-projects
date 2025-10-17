
"""
This package contains document parsers for various file formats.
"""

from .base import parser_registry, BaseDocumentParser
from .pdf_parser import PDFParser
from .txt_parser import TxtParser

# Register the parsers
parser_registry.register(PDFParser())
parser_registry.register(TxtParser())

__all__ = ["parser_registry", "BaseDocumentParser"]
