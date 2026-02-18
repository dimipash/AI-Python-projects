# AI Voice Assistant - Backend

This directory contains the backend code for the AI Voice Assistant project, built using Python and Flask.

## Features

- Real-time audio processing
- Speech-to-text conversion
- Natural language understanding
- Integration with AI models
- REST API endpoints for frontend communication

## Technologies

- Python 3.10+
- Flask


## Setup

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Environment variables:**

    Create a `.env` file in the `backend` directory with these variables:

    ```env
    OPENAI_API_KEY=your_api_key_here
    PORT=5000
    DEBUG=True
    ```

3. **Run the server:**

    ```bash
    python main.py
    ```

    The API will be available at `http://localhost:5000`

## API Documentation

### Endpoints

- `POST /api/transcribe` - Audio transcription
- `POST /api/process` - Natural language processing
- `GET /api/status` - Service health check

[Add more detailed API documentation here]

## Screenshots


