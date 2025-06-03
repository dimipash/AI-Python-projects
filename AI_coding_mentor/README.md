# AI Coding Mentor

An interactive AI-powered learning platform designed to help you master coding concepts.

## Overview

The AI Coding Mentor is a web application built with Python and Streamlit that provides structured learning roadmaps, interactive quizzes, a resource library with vector search, and an AI chat assistant. It uses MongoDB for data storage and integrates with the Parlant AI platform.

## Key Features

*   **Learning Roadmaps:** Structured paths to guide your learning.
*   **Interactive Quizzes:** Test your knowledge with engaging quizzes.
*   **Resource Library:** Find relevant coding resources using natural language search.
*   **AI Chat Assistant:** Get help and explanations from an AI tutor.

## Technologies

*   Python, Streamlit
*   MongoDB
*   Vector Search (Sentence Transformers)
*   Parlant SDK

## How to Run

1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Set up MongoDB credentials in a `.env` file.
4.  Install the private `parlant-sdk`.
5.  Create a vector search index in MongoDB (run `db.create_index()` from `database.py`).
6.  Create agents in Parlant and update the agent ID in the chat component.
7.  Run the app: `streamlit run pages/1_Roadmap.py`
8.  Open your browser to `http://localhost:8501`.
