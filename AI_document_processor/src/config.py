"""
Configuration management for AI Document Processing System.
Handles environment variables and application settings.
"""

import os
from typing import List, Optional
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    """Application settings and configuration."""

    # API Keys
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None

    # Model Configuration
    openai_model: str = "gpt-3.5-turbo"
    gemini_model: str = "gemini-pro"
    embedding_model: str = "text-embedding-ada-002"
    sentence_transformer_model: str = "all-MiniLM-L6-v2"

    # OCR Configuration
    tesseract_cmd: str = "/usr/bin/tesseract"
    tesseract_data_path: str = "/usr/share/tesseract-ocr/4.00/tessdata"

    # Vector Database Configuration
    chroma_persist_directory: str = "./chroma_db"
    chroma_host: str = "localhost"
    chroma_port: int = 8000

    # Redis Configuration
    redis_url: str = "redis://localhost:6379/0"

    # Application Configuration
    debug: bool = False
    log_level: str = "INFO"
    max_file_size_mb: int = 50
    supported_extensions: str = ".pdf,.docx,.txt,.png,.jpg,.jpeg,.tiff"

    # Processing Configuration
    chunk_size: int = 1000
    chunk_overlap: int = 200
    max_summary_length: int = 500
    batch_size: int = 5

    # Security
    secret_key: str = "your-secret-key-change-this"
    allowed_origins: str = "http://localhost:3000,http://localhost:8501"

    # Storage Directories
    upload_dir: str = "./uploads"
    processed_dir: str = "./processed"
    temp_dir: str = "./temp"

    # Feature Flags
    enable_ocr: bool = True
    enable_classification: bool = True
    enable_sentiment_analysis: bool = True
    enable_entity_extraction: bool = True
    enable_batch_processing: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False

    @validator("supported_extensions")
    def parse_supported_extensions(cls, v):
        """Parse supported extensions into a list."""
        if isinstance(v, str):
            return [ext.strip() for ext in v.split(",")]
        return v

    @validator("allowed_origins")
    def parse_allowed_origins(cls, v):
        """Parse allowed origins into a list."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v

    @property
    def supported_file_extensions(self) -> List[str]:
        """Get list of supported file extensions."""
        if isinstance(self.supported_extensions, str):
            return [ext.strip() for ext in self.supported_extensions.split(",")]
        return self.supported_extensions

    @property
    def allowed_origins_list(self) -> List[str]:
        """Get list of allowed origins."""
        if isinstance(self.allowed_origins, str):
            return [origin.strip() for origin in self.allowed_origins.split(",")]
        return self.allowed_origins

    def create_directories(self):
        """Create necessary directories if they don't exist."""
        directories = [
            self.upload_dir,
            self.processed_dir,
            self.temp_dir,
            self.chroma_persist_directory,
        ]

        for directory in directories:
            os.makedirs(directory, exist_ok=True)

    def validate_setup(self) -> bool:
        """Validate that required configuration is present."""
        if not self.openai_api_key and not self.gemini_api_key:
            raise ValueError(
                "At least one AI API key (OpenAI or Gemini) must be provided"
            )

        return True


# Global settings instance
settings = Settings()

# Initialize directories on import
try:
    settings.create_directories()
except Exception as e:
    print(f"Warning: Could not create directories: {e}")
