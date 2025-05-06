# LangGraph Agent

A dual-personality chatbot agent built with LangGraph and LangChain, powered by Anthropic's Claude 3.5 Sonnet model.

## Description

This project implements an intelligent conversational agent using LangGraph's StateGraph for orchestration and Claude 3.5 Sonnet as the underlying language model. The agent can analyze user messages and dynamically switch between two different response modes (emotional or logical) based on the content and intent of the user's input.

## Features

- **Message Classification**: Automatically classifies user messages as either "emotional" or "logical" using Claude 3.5 Sonnet
- **Dual-Agent System**:
  - **Therapist Agent**: Responds to emotional queries with empathy, validation, and emotional support
  - **Logical Agent**: Responds to factual queries with direct, evidence-based information
- **Dynamic Routing**: Routes messages to the appropriate agent based on message classification
- **Conversational Memory**: Maintains conversation history for context-aware responses

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

The script will prompt you to enter a message. The agent will:
1. Analyze your message to determine if it requires an emotional or logical response
2. Route your message to either the therapist agent or the logical agent
3. Provide a response tailored to the nature of your query

Examples:
- Emotional queries (e.g., "I'm feeling really stressed about my job") will receive empathetic, supportive responses
- Logical queries (e.g., "What are the main causes of climate change?") will receive factual, informative responses

Type `exit` to end the conversation.

## Project Structure

- `main.py` - The main script containing:
  - Message classification logic
  - Therapist and logical agent implementations
  - LangGraph state management and routing
  - User interaction loop
- `pyproject.toml` - Project configuration and dependencies
- `.env` - Environment variables (not tracked in git)
- `README.md` - Project documentation
