# DataGen Agent: AI-Powered Synthetic Data Generator

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DataGen Agent is a sophisticated, command-line-driven AI agent designed to generate realistic, synthetic user data based on natural language instructions. Built with Python, LangChain, and OpenAI, it provides a conversational interface for creating and managing sample datasets effortlessly.

## Overview

This agent leverages the power of Large Language Models (LLMs) through the LangChain and LangGraph frameworks to create a ReAct-style agent. It can understand complex requests, use custom-built tools to generate data, and interact with the local filesystem to read and write JSON files. It's an ideal tool for developers, testers, and data scientists who need to quickly create mock data for their applications.

## Features

-   **Interactive CLI:** A user-friendly command-line interface for conversational data generation.
-   **Natural Language Understanding:** Simply describe the data you need, and the agent will generate it.
-   **Custom Data Generation:** Creates users with specified names, email domains, and age ranges.
-   **File System Integration:** Seamlessly saves generated data to well-formatted JSON files and can read existing data.
-   **Extensible Toolset:** The agent's capabilities can be easily expanded by adding new tools.

## Technology Stack

-   **Core:** Python 3.13+
-   **AI Framework:** LangChain, LangGraph
-   **LLM Provider:** OpenAI (GPT-4)
-   **Environment Management:** `uv`
-   **Configuration:** `python-dotenv`

## Getting Started

Follow these instructions to get the DataGen Agent running on your local machine.

### Prerequisites

-   Python 3.13 or higher
-   `uv` installed (`pip install uv`)
-   An OpenAI API Key

### Installation & Configuration

1.  **Clone this repository.**   

2.  **Install dependencies:**
    Create the virtual environment and install all required packages using `uv`.
    ```bash
    uv sync
    ```

3.  **Set up your environment:**
    Copy the sample environment file and add your OpenAI API key.
    ```bash
    cp .env.sample .env
    ```
    Now, open `.env` and add your key:
    ```
    OPENAI_API_KEY="your-openai-api-key-here"
    ```

## Usage

To start the agent, run the `main.py` script from your terminal.

```bash
uv run python main.py
```

The agent will greet you and await your instructions.

### Example Prompts

Here are a few examples of what you can ask the agent to do:

-   `Generate users named John, Jane, and Mike and save to users.json`
-   `Create 5 users with the last names Smith and Jones`
-   `Make users aged 25-35 with company.com and business.org emails, then write them to a file named new_staff.json`
-   `read the users from users.json`

To exit the agent, simply type `quit` or `exit`.

## How It Works

The agent operates on a ReAct (Reasoning and Acting) model, orchestrated by LangGraph.

1.  **Input:** The user provides a prompt in the CLI.
2.  **Reasoning:** The LLM (GPT-4) receives the user prompt, the conversation history, and a system message that defines its persona and available tools. It then decides whether to use a tool or respond directly to the user.
3.  **Action:** If a tool is chosen, the agent executes it (e.g., `generate_sample_users`, `write_json`).
4.  **Observation:** The output of the tool is fed back to the LLM.
5.  **Response:** The LLM uses the tool's output to formulate a final, human-readable response, which is then printed to the console.

This loop continues, allowing for multi-step, tool-augmented conversations.

