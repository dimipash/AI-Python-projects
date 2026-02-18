# AI Voice Assistant - Frontend

This directory contains the frontend code for the AI Voice Assistant project, built using React and Vite.

## Features

- Real-time voice interaction interface
- Speech visualization components
- Call management interface
- Responsive design
- WebSocket integration for real-time updates

## Technologies

- React 18+
- Vite

## Setup

1. **Install dependencies:**

    ```bash
    npm install
    ```

2. **Environment variables:**

    Create a `.env` file in the `frontend` directory with these variables:

    ```env
    VITE_API_URL=http://localhost:5000
    VITE_WS_URL=ws://localhost:5000/ws
    ```

3. **Run the development server:**

    ```bash
    npm run dev
    ```

    The application will be available at `http://localhost:5173`

## Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── call/            # Call-related components
│   ├── App.jsx          # Main application component
│   ├── main.jsx         # Application entry point
│   └── index.css        # Global styles
```




