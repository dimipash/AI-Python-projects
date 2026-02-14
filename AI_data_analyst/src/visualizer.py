import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional
import numpy as np


class DataVisualizer:
    """Generate visualizations from data."""

    def __init__(self, data: pd.DataFrame, output_dir: str = "outputs"):
        self.data = data
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        sns.set_style("whitegrid")
        plt.rcParams["figure.figsize"] = (10, 6)

    def histogram(self, column: str, bins: int = 30) -> str:
        """Create histogram for a numeric column."""
        if column not in self.data.columns:
            raise ValueError(f"Column not found: {column}")

        col = self.data[column]
        if not pd.api.types.is_numeric_dtype(col):
            raise ValueError(f"Column {column} is not numeric")

        fig, ax = plt.subplots()
        ax.hist(col.dropna(), bins=bins, edgecolor="black", alpha=0.7)
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        ax.set_title(f"Distribution of {column}")

        path = self.output_dir / f"histogram_{column}.png"
        plt.savefig(path, dpi=150, bbox_inches="tight")
        plt.close()

        return str(path)

    def bar_chart(self, column: str, top_n: int = 20) -> str:
        """Create bar chart for categorical column."""
        if column not in self.data.columns:
            raise ValueError(f"Column not found: {column}")

        counts = self.data[column].value_counts().head(top_n)

        fig, ax = plt.subplots()
        counts.plot(kind="bar", ax=ax, color="steelblue", edgecolor="black")
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        ax.set_title(f"Top {top_n} values in {column}")
        ax.tick_params(axis="x", rotation=45)

        path = self.output_dir / f"bar_{column}.png"
        plt.savefig(path, dpi=150, bbox_inches="tight")
        plt.close()

        return str(path)

    def correlation_heatmap(self) -> Optional[str]:
        """Create correlation heatmap for numeric columns."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) < 2:
            return None

        corr = self.data[numeric_cols].corr()

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(
            corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax, square=True
        )
        ax.set_title("Correlation Matrix")

        path = self.output_dir / "correlation_heatmap.png"
        plt.savefig(path, dpi=150, bbox_inches="tight")
        plt.close()

        return str(path)

    def scatter_plot(self, x: str, y: str) -> str:
        """Create scatter plot for two numeric columns."""
        if x not in self.data.columns or y not in self.data.columns:
            raise ValueError(f"Column not found")

        fig, ax = plt.subplots()
        ax.scatter(self.data[x], self.data[y], alpha=0.5)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")

        path = self.output_dir / f"scatter_{x}_vs_{y}.png"
        plt.savefig(path, dpi=150, bbox_inches="tight")
        plt.close()

        return str(path)

    def box_plot(self, column: str) -> str:
        """Create box plot for numeric column."""
        if column not in self.data.columns:
            raise ValueError(f"Column not found: {column}")

        fig, ax = plt.subplots()
        self.data[column].dropna().plot(kind="box", ax=ax)
        ax.set_ylabel(column)
        ax.set_title(f"Box Plot of {column}")

        path = self.output_dir / f"boxplot_{column}.png"
        plt.savefig(path, dpi=150, bbox_inches="tight")
        plt.close()

        return str(path)
