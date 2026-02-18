import pandas as pd
from pathlib import Path
from typing import Optional


class DataLoader:
    """Handles loading data from various file formats."""

    def __init__(self):
        self.data: Optional[pd.DataFrame] = None
        self.file_path: Optional[Path] = None

    def load(self, file_path: str) -> pd.DataFrame:
        """Load data from CSV or Excel file.

        Args:
            file_path: Path to the data file

        Returns:
            Loaded DataFrame

        Raises:
            ValueError: If file format is not supported
            FileNotFoundError: If file doesn't exist
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        self.file_path = path
        suffix = path.suffix.lower()

        if suffix == ".csv":
            self.data = self._load_csv(path)
        elif suffix in [".xlsx", ".xls"]:
            self.data = self._load_excel(path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")

        return self.data

    def _load_csv(self, path: Path) -> pd.DataFrame:
        """Load CSV with auto-detection of encoding and delimiter."""
        encodings = ["utf-8", "latin-1", "cp1252"]
        delimiters = [",", ";", "\t", "|"]

        for encoding in encodings:
            for delimiter in delimiters:
                try:
                    return pd.read_csv(
                        path,
                        encoding=encoding,
                        delimiter=delimiter,
                        encoding_errors="replace",
                    )
                except Exception:
                    continue

        raise ValueError(f"Could not read CSV file: {path}")

    def _load_excel(self, path: Path) -> pd.DataFrame:
        """Load Excel file."""
        return pd.read_excel(path, engine="openpyxl")

    def get_info(self) -> dict:
        """Get basic info about loaded data."""
        if self.data is None:
            return {"status": "No data loaded"}

        return {
            "rows": len(self.data),
            "columns": len(self.data.columns),
            "column_names": list(self.data.columns),
            "dtypes": {col: str(dtype) for col, dtype in self.data.dtypes.items()},
            "memory_usage_mb": round(
                self.data.memory_usage(deep=True).sum() / 1024 / 1024, 2
            ),
        }
