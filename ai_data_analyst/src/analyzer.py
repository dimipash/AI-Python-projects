import pandas as pd
import numpy as np
from typing import Optional


class DataAnalyzer:
    """Statistical analysis of loaded data."""

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def describe_column(self, column: str) -> dict:
        """Get detailed statistics for a single column."""
        if column not in self.data.columns:
            raise ValueError(f"Column not found: {column}")

        col = self.data[column]

        result = {
            "name": column,
            "dtype": str(col.dtype),
            "count": int(col.count()),
            "nulls": int(col.isnull().sum()),
            "unique": int(col.nunique()),
        }

        if pd.api.types.is_numeric_dtype(col):
            result.update(
                {
                    "mean": round(float(col.mean()), 4),
                    "median": round(float(col.median()), 4),
                    "std": round(float(col.std()), 4),
                    "min": round(float(col.min()), 4),
                    "max": round(float(col.max()), 4),
                    "q25": round(float(col.quantile(0.25)), 4),
                    "q75": round(float(col.quantile(0.75)), 4),
                }
            )

        if col.dtype == "object" or pd.api.types.is_categorical_dtype(col):
            value_counts = col.value_counts().head(10)
            result["top_values"] = {str(k): int(v) for k, v in value_counts.items()}

        return result

    def describe_all(self) -> dict:
        """Get statistics for all columns."""
        stats = {}
        for col in self.data.columns:
            try:
                stats[col] = self.describe_column(col)
            except Exception as e:
                stats[col] = {"error": str(e)}
        return stats

    def get_correlation(self) -> Optional[pd.DataFrame]:
        """Get correlation matrix for numeric columns."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) < 2:
            return None
        return self.data[numeric_cols].corr()

    def get_data_types(self) -> dict:
        """Categorize columns by data type."""
        return {
            "numeric": list(self.data.select_dtypes(include=[np.number]).columns),
            "categorical": list(
                self.data.select_dtypes(include=["object", "category"]).columns
            ),
            "datetime": list(self.data.select_dtypes(include=["datetime64"]).columns),
            "boolean": list(self.data.select_dtypes(include=["bool"]).columns),
        }

    def get_summary(self) -> dict:
        """Get a quick summary of the dataset."""
        return {
            "rows": len(self.data),
            "columns": len(self.data.columns),
            "missing_values": int(self.data.isnull().sum().sum()),
            "duplicate_rows": int(self.data.duplicated().sum()),
            "dtypes": self.get_data_types(),
        }
