# LangGraph Agent

A simple chatbot agent built with LangGraph and LangChain, powered by Anthropic's Claude 3.5 Sonnet model.

## Description

This project implements a basic conversational agent using LangGraph's StateGraph for orchestration and Claude 3.5 Sonnet as the underlying language model. The agent can respond to user inputs in a conversational manner.

## Technologies Used

- Python 3.13+
- LangGraph 0.4.1+ - For agent orchestration and state management
- LangChain 0.3.25+ - For LLM integration
- Anthropic Claude 3.5 Sonnet - As the language model
- python-dotenv - For environment variable management

## Setup

### Prerequisites

- Python 3.13 or higher
- Anthropic API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   or
   ```
   pip install langchain[anthropic] langgraph python-dotenv ipykernel
   ```

3. Create a `.env` file in the project root with your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

Run the main script:

```
python main.py
```

The script will prompt you to enter a message, and the agent will respond using Claude 3.5 Sonnet.

## Project Structure

- `main.py` - The main script that initializes the LangGraph agent and handles user interaction
- `pyproject.toml` - Project configuration and dependencies
- `.env` - Environment variables (not tracked in git)
- `README.md` - Project documentation

