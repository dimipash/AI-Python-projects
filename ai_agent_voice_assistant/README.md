# Voice AI Agent Demo

This project is a simple demonstration of a Voice AI agent, utilizing Flask for the backend and React for the frontend. It showcases basic voice call functionality integrated with a simple backend API.

## Features

- **Voice Call Integration:**  Initiate and terminate voice calls using the Vapi.ai web library in the frontend.
- **Order Retrieval (Backend):** Provides an API endpoint to fetch order details based on an order number. (Currently uses a hardcoded database for demonstration purposes).

## Tech Stack

- **Frontend:**
    - React
    - Vite
    - @vapi-ai/web

- **Backend:**
    - Flask (Python)

## Setup

### Backend

1.  Navigate to the project's root directory (`ai_agent_voice_assistant`).
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    ```bash
    venv\\Scripts\\activate  # Windows
    # source venv/bin/activate # macOS/Linux
    ```
4.  Install backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the Flask API:
    ```bash
    python api.py
    ```

### Frontend

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install frontend dependencies:
    ```bash
    npm install
    ```
3.  Run the React app:
    ```bash
    npm run dev
    ```

## Usage

1.  Ensure both the backend Flask API and the frontend React app are running.
2.  Open the React app in your web browser (typically `http://localhost:5173`).
3.  Click the "Start Call" button to begin a voice call session.
4.  Click the "Stop Call" button to end the active voice call.


