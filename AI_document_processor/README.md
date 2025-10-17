# AI Document Analysis & Processing System

An intelligent document processing system that leverages AI and OCR technologies to analyze, extract, and understand information from various document formats.

## 🌟 Features

- **Multi-format Support**: Process PDF, DOCX, TXT, and image files
- **OCR Integration**: Extract text from images and scanned documents
- **Document Summarization**: AI-powered document summarization
- **Question Answering**: Ask questions about your documents
- **Classification**: Automatically categorize documents
- **Metadata Extraction**: Extract key information and entities
- **Web Interface**: User-friendly Streamlit dashboard
- **Batch Processing**: Process multiple documents simultaneously

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │   API Gateway   │    │  Processing     │
│   (Streamlit)   │────│   (FastAPI)     │────│   Workers       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                       │
                                │                       │
                       ┌─────────────────┐    ┌─────────────────┐
                       │   Document      │    │   AI Services   │
                       │   Storage       │    │   (LLM/OCR)     │
                       └─────────────────┘    └─────────────────┘
```

## 🛠️ Technologies

- **Backend**: Python 3.9+, FastAPI
- **Frontend**: Streamlit
- **AI/ML**: OpenAI API, Google Gemini, Tesseract OCR
- **Document Processing**: PyMuPDF, python-docx, Pillow
- **Vector Storage**: ChromaDB (for semantic search)
- **Task Queue**: Celery with Redis (optional for async processing)

## 🚀 Quick Start

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. Run the web interface:
   ```bash
   streamlit run streamlit_app.py
   ```

5. Or start the API server:
   ```bash
   uvicorn main:app --reload
   ```

## 📁 Project Structure

```
AI_document_processor/
├── src/
│   ├── parsers/          # Document parsers
│   ├── services/         # AI services (OCR, LLM)
│   ├── storage/          # Document storage
│   └── utils/            # Utilities
├── web/                  # Streamlit web interface
├── api/                  # FastAPI endpoints
├── tests/                # Test files
├── data/                 # Sample documents
├── main.py              # FastAPI application
├── streamlit_app.py     # Streamlit interface
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## 📖 Usage

### Web Interface
1. Upload documents through the Streamlit interface
2. Choose processing options (OCR, summarization, etc.)
3. View results and interact with processed documents

### API Usage
```python
import requests

# Upload and process a document
files = {'file': open('document.pdf', 'rb')}
response = requests.post('http://localhost:8000/process', files=files)
```

## 🔧 Configuration

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
TESSERACT_CMD=/usr/bin/tesseract  # Path to Tesseract OCR
CHROMA_PERSIST_DIRECTORY=./chroma_db
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT models
- Google for Gemini AI
- Tesseract for OCR capabilities
- Streamlit for the web interface