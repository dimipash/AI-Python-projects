# RAG Production App

This is a Retrieval-Augmented Generation (RAG) application built with FastAPI and Inngest.

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for package management

### Installation

1.  Create a virtual environment:
    ```bash
    uv venv
    ```
2.  Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    uv pip install -r requirements.txt
    ```

### Running the Application

1.  Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2.  Start the Inngest development server in a separate terminal:
    ```bash
    npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
    ```
