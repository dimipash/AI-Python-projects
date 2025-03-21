# AI Voice Assistant Project

This project is an AI Voice Assistant application built with a frontend in React and a backend in Python.

## Project Structure

The project is structured into two main directories:

-   **frontend**: Contains the React frontend application.
-   **backend**: Contains the Python backend application.

### Frontend

The frontend is located in the `frontend` directory and is built using React and Vite.

-   `.env-sample`: Sample environment variables for the frontend.
-   `.gitignore`: Git ignore file for the frontend.
-   `eslint.config.js`: ESLint configuration for the frontend.
-   `index.html`: Main HTML file for the frontend.
-   `package.json`: npm package file for the frontend.
-   `README.md`: README file for the frontend (if any).
-   `vite.config.js`: Vite configuration file for the frontend.
-   `public/`: Public assets for the frontend.
    -   `vite.svg`: Vite logo.
-   `src/`: Source code for the frontend.
    -   `ai.js`:  Likely contains AI related logic for the frontend.
    -   `App.jsx`: Main App component.
    -   `index.css`: Global styles.
    -   `main.jsx`: Entry point for the React application.
    -   `call/`: Components related to call functionality.
        -   `ActiveCallDetails.jsx`: Component for displaying active call details.
        -   `AssistantSpeechIndicator.jsx`: Component for indicating assistant speech.
        -   `VolumeLevel.jsx`: Component for displaying volume level.

### Backend

The backend is located in the `backend` directory and is built using Python.

-   `.env-sample`: Sample environment variables for the backend.
-   `main.py`: Main Python application file.
-   `README.md`: README file for the backend (if any).
-   `requirements.txt`: Python dependencies for the backend.

## Setup Instructions

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   **Windows:** `venv\Scripts\activate`
    -   **macOS/Linux:** `source venv/bin/activate`
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Create a `.env` file based on `.env-sample` and configure environment variables as needed.

### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Create a `.env` file based on `.env-sample` and configure environment variables as needed.

## Running the Application

### Run Backend

1.  Navigate to the `backend` directory and activate the virtual environment if you haven't already.
2.  Run the backend application:
    ```bash
    python main.py
    ```

### Run Frontend

1.  Navigate to the `frontend` directory.
2.  Start the frontend development server:
    ```bash
    npm run dev
    ```
    This will typically start the frontend on `http://localhost:5173` or a similar address.


