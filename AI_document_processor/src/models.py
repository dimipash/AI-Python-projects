"""
Data models and schemas for AI Document Processing System.
Defines the core data structures used throughout the application.
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator
import uuid


class DocumentType(str, Enum):
    """Supported document types."""

    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    IMAGE = "image"
    UNKNOWN = "unknown"


class ProcessingStatus(str, Enum):
    """Document processing status."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class DocumentMetadata(BaseModel):
    """Document metadata extracted from files."""

    title: Optional[str] = None
    author: Optional[str] = None
    subject: Optional[str] = None
    creator: Optional[str] = None
    producer: Optional[str] = None
    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None
    page_count: Optional[int] = None
    word_count: Optional[int] = None
    language: Optional[str] = None
    keywords: List[str] = Field(default_factory=list)
    file_size: Optional[int] = None

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class ProcessingOptions(BaseModel):
    """Options for document processing."""

    enable_ocr: bool = True
    enable_summarization: bool = True
    enable_classification: bool = True
    enable_entity_extraction: bool = True
    enable_sentiment_analysis: bool = True
    chunk_size: int = 1000
    chunk_overlap: int = 200
    max_summary_length: int = 500
    extract_images: bool = False
    preserve_layout: bool = True


class DocumentChunk(BaseModel):
    """A chunk of text from a document."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    document_id: str
    chunk_index: int
    content: str
    page_number: Optional[int] = None
    start_char: Optional[int] = None
    end_char: Optional[int] = None
    embedding: Optional[List[float]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        json_encoders = {bytes: lambda v: v.hex() if v else None}


class ExtractedEntity(BaseModel):
    """An entity extracted from document text."""

    text: str
    label: str  # PERSON, ORGANIZATION, LOCATION, DATE, etc.
    confidence: float
    start_pos: int
    end_pos: int
    context: str


class SentimentResult(BaseModel):
    """Sentiment analysis result."""

    sentiment: str  # positive, negative, neutral
    confidence: float
    scores: Dict[str, float]  # detailed scores for each sentiment


class DocumentSummary(BaseModel):
    """Document summary information."""

    short_summary: str  # 1-2 sentences
    detailed_summary: str  # longer summary
    key_points: List[str]
    topics: List[str]
    sentiment: Optional[SentimentResult] = None
    language: Optional[str] = None
    model_used: str


class ClassificationResult(BaseModel):
    """Document classification result."""

    category: str
    subcategory: Optional[str] = None
    confidence: float
    categories: Dict[str, float]  # all category scores
    tags: List[str] = Field(default_factory=list)


class Document(BaseModel):
    """Main document model."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str
    file_path: str
    file_type: DocumentType
    file_size: int
    content: str
    metadata: DocumentMetadata
    processing_status: ProcessingStatus = ProcessingStatus.PENDING
    processing_options: ProcessingOptions
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    processed_at: Optional[datetime] = None

    # Processing results
    summary: Optional[DocumentSummary] = None
    classification: Optional[ClassificationResult] = None
    entities: List[ExtractedEntity] = Field(default_factory=list)
    sentiment: Optional[SentimentResult] = None
    chunks: List[DocumentChunk] = Field(default_factory=list)

    # Error handling
    error_message: Optional[str] = None
    processing_log: List[str] = Field(default_factory=list)

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}

    @validator("filename")
    def validate_filename(cls, v):
        """Validate filename."""
        if not v or len(v.strip()) == 0:
            raise ValueError("Filename cannot be empty")
        return v.strip()

    @validator("file_size")
    def validate_file_size(cls, v):
        """Validate file size."""
        if v < 0:
            raise ValueError("File size cannot be negative")
        return v

    def add_processing_log(self, message: str):
        """Add a log entry to the processing log."""
        timestamp = datetime.utcnow().isoformat()
        log_entry = f"[{timestamp}] {message}"
        self.processing_log.append(log_entry)

    def update_status(
        self, status: ProcessingStatus, error_message: Optional[str] = None
    ):
        """Update document processing status."""
        self.processing_status = status
        self.updated_at = datetime.utcnow()

        if status == ProcessingStatus.COMPLETED:
            self.processed_at = datetime.utcnow()

        if error_message:
            self.error_message = error_message
            self.add_processing_log(f"ERROR: {error_message}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert document to dictionary."""
        return self.dict()


class ProcessingJob(BaseModel):
    """Document processing job information."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    document_id: str
    job_type: str  # "process", "summarize", "classify", etc.
    status: ProcessingStatus = ProcessingStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    progress: float = 0.0  # 0.0 to 1.0
    message: Optional[str] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class QueryRequest(BaseModel):
    """Request for document query."""

    query: str
    document_ids: Optional[List[str]] = None
    limit: int = 10
    min_similarity: float = 0.7
    include_metadata: bool = True


class QueryResult(BaseModel):
    """Result from document query."""

    document_id: str
    chunk_id: str
    content: str
    score: float
    metadata: Dict[str, Any]
    document_info: Optional[Dict[str, Any]] = None


class BulkProcessRequest(BaseModel):
    """Request for bulk document processing."""

    document_paths: List[str]
    options: ProcessingOptions
    parallel: bool = False
    max_workers: int = 4


class SystemStatus(BaseModel):
    """System status information."""

    total_documents: int
    processing_documents: int
    completed_documents: int
    failed_documents: int
    storage_used_mb: float
    uptime: str
    version: str
    features_enabled: Dict[str, bool]
