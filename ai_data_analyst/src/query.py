import os
import json
from openai import OpenAI
from typing import Optional
import pandas as pd


class DataQuery:
    """Answer natural language questions about data using LLM."""

    def __init__(self, api_key: Optional[str] = None):
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY env var or pass as parameter."
            )

        self.client = OpenAI(api_key=api_key)

    def ask(self, question: str, data: pd.DataFrame) -> str:
        """Answer a question about the data."""
        context = self._build_context(data)

        prompt = f"""You are a data analyst. Based on the following dataset information, answer the user's question.

Dataset Summary:
{context}

User Question: {question}

Provide a clear, concise answer. If calculations are needed, show the result. Format any data as a table if helpful."""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful data analyst assistant.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content

    def _build_context(self, data: pd.DataFrame) -> str:
        """Build context string from data for the LLM."""
        lines = []
        lines.append(f"Shape: {data.shape[0]} rows, {data.shape[1]} columns\n")

        lines.append("Columns:")
        for col in data.columns:
            dtype = str(data[col].dtype)
            nulls = data[col].isnull().sum()
            lines.append(f"  - {col}: {dtype} ({nulls} nulls)")

        lines.append("\nSample data (first 5 rows):")
        lines.append(data.head().to_string())

        lines.append("\nNumeric column statistics:")
        numeric = data.select_dtypes(include=["number"]).columns
        if len(numeric) > 0:
            lines.append(data[numeric].describe().to_string())

        return "\n".join(lines)
