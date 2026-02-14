# AI Python Projects

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

This repository contains a collection of small to medium-sized projects focused on exploring various applications of Artificial Intelligence (AI) using Python and related technologies.

## Key Features

*   **Diverse AI Applications:** Explore a wide range of AI use cases, from web scraping and research to voice assistants, coding mentors, and data analysis.
*   **Modern Technologies:** Each project utilizes current and relevant Python libraries and frameworks, including LangChain, FastAPI, Streamlit, and more.
*   **Modular and Understandable:** The projects are structured to be clear, modular, and easy to understand, making them great for learning and experimentation.
*   **Practical Examples:** Get hands-on with practical examples that you can adapt and build upon for your own AI projects.

## Project Structure

Each project is contained in its own directory, and includes a `README.md` with specific setup and usage instructions. The general structure is as follows:

```
/AI-Python-projects
|-- /AI_agent_research
|-- /AI_agent_voice_assistant
|-- /AI_coding_mentor
|-- /AI_data_analyst
|-- /AI_scraper_agent
|-- /AI_voice_assistant
|-- /ChatGPT_Apps_sdk
|-- /custom_mcp_server
|-- /langflow_web_agent
|-- /langgraph_agent
|-- /Python_coding_agent
|-- /RAG_production_app
|-- /Reddit_scraping_pipeline
|-- /simple_AI_agent
|-- README.md
```

## Technologies

The projects in this repository utilize a variety of modern technologies, including:

*   **Python 3.7+**
*   **AI & Machine Learning:** LangChain, TensorFlow, PyTorch, Scikit-learn, OpenAI API, Google Gemini API
*   **Web Frameworks:** FastAPI, Flask, Django, Streamlit
*   **Frontend:** React, Vite
*   **Databases:** MongoDB, PostgreSQL
*   **Other Tools:** Docker, Git, Poetry, Pipenv

## Projects

*   [AI Agent Research (`AI_agent_research/`)](#ai-agent-research-ai_agent_research)
*   [AI Agent Voice Assistant (`AI_agent_voice_assistant/`)](#ai-agent-voice-assistant-ai_agent_voice_assistant)
*   [AI Coding Mentor (`AI_coding_mentor/`)](#ai-coding-mentor-ai_coding_mentor)
*   [AI Data Analyst (`AI_data_analyst/`)](#ai-data-analyst-ai_data_analyst)
*   [AI Scraper Agent (`AI_scraper_agent/`)](#ai-scraper-agent-ai_scraper_agent)
*   [AI Voice Assistant (`AI_voice_assistant/`)](#ai-voice-assistant-ai_voice_assistant)
*   [ChatGPT Apps SDK (`ChatGPT_Apps_sdk/`)](#chatgpt-apps-sdk-chatgpt_apps_sdk)
*   [Custom MCP Server (`custom_mcp_server/`)](#custom-mcp-server-custom_mcp_server)
*   [Langflow Web Agent (`langflow_web_agent/`)](#langflow-web-agent-langflow_web_agent)
*   [Langgraph Agent (`langgraph_agent/`)](#langgraph-agent-langgraph_agent)
*   [Python Coding Agent (`Python_coding_agent/`)](#python-coding-agent-python_coding_agent)
*   [RAG Production App (`RAG_production_app/`)](#rag-production-app-rag_production_app)
*   [Reddit Scraping Pipeline (`Reddit_scraping_pipeline/`)](#reddit-scraping-pipeline-reddit_scraping_pipeline)
*   [Simple AI Agent (`simple_AI_agent/`)](#simple-ai-agent-simple_ai_agent)

Below is a brief overview of the projects included in this repository:

### AI Agent Research (`AI_agent_research/`)

*   **Description:** A research assistant agent built with LangChain. It takes a user query, utilizes tools like web search (Tavily) and Wikipedia, and generates a research summary with sources. It supports different LLMs (Claude, GPT) and saves the output.
*   **Key Technologies:** Python, LangChain, Langchain-OpenAI, Langchain-Anthropic, Tavily Search, Wikipedia, Pydantic.

### AI Agent Voice Assistant (`AI_agent_voice_assistant/`)

*   **Description:** A demonstration of a Voice AI agent capable of handling voice calls. It features a simple backend API for tasks like order retrieval and integrates with Vapi.ai for voice functionality.
*   **Key Technologies:** Python, Flask (Backend), React, Vite, @vapi-ai/web (Frontend).

### AI Coding Mentor (`AI_coding_mentor/`)

*   **Description:** An interactive AI-powered learning platform designed to help users master coding concepts. It offers structured learning roadmaps, interactive quizzes, a searchable resource library (using vector search), and an AI chat assistant integrated via the Parlant platform.
*   **Key Technologies:** Python, Streamlit, MongoDB, Pymongo, Sentence Transformers, Pydantic, Parlant SDK.

### AI Data Analyst (`AI_data_analyst/`)

*   **Description:** A CLI tool for data analysis with natural language queries. Load CSV/Excel files, generate statistics, visualizations, and ask questions about your data using OpenAI GPT.
*   **Key Technologies:** Python, pandas, matplotlib, seaborn, OpenAI API, Click.

### AI Scraper Agent (`AI_scraper_agent/`)

*   **Description:** An AI agent designed to scrape web data, specifically demonstrated by extracting the latest posts from a specified Instagram profile using browser automation.
*   **Key Technologies:** Python, Langchain-Anthropic, browser-use (Playwright), Pydantic.

### AI Voice Assistant (`AI_voice_assistant/`)

*   **Description:** A general-purpose AI voice assistant application. It includes a backend for real-time audio processing, speech-to-text, and natural language understanding (using OpenAI), and a frontend for user interaction.
*   **Key Technologies:** Python, Flask (Backend), OpenAI API, React, Vite (Frontend).

### ChatGPT Apps SDK (`ChatGPT_Apps_sdk/`)

*   **Description:** This project is a Python-based web service that demonstrates the use of the FastMCP library to create a tool-use MCP (Multi-turn Conversation Protocol) application. The project also includes a FastAPI web application that exposes both regular API endpoints and the MCP application.
*   **Key Technologies:** Python, FastAPI, FastMCP, Uvicorn, Rav.

### Custom MCP Server (`custom_mcp_server/`)

*   **Description:** A custom Model Context Protocol (MCP) server demonstrating how to extend the agent's capabilities with new tools and resources. This project provides a template and example for creating your own MCP servers to integrate with the AI agent framework.
*   **Key Technologies:** Python, FastAPI, MCP.

### Langflow Web Agent (`langflow_web_agent/`)

*   **Description:** A powerful web scraping and data extraction tool built with Langflow, leveraging Bright Data's Web Unlocker and Dataset APIs to provide intelligent web data collection capabilities.
*   **Key Technologies:** Python, Langflow, Bright Data.

### Langgraph Agent (`langgraph_agent/`)

*   **Description:** An AI agent project utilizing Langgraph to build stateful, multi-actor applications with large language models.
*   **Key Technologies:** Python, Langgraph, LangChain.

### Python Coding Agent (`Python_coding_agent/`)

*   **Description:** A command-line tool that leverages Google's Gemini AI to act as an intelligent coding agent. It can perform file operations (list, read, write) and execute Python scripts based on natural language prompts.
*   **Key Technologies:** Python, Google Gemini API.

### RAG Production App (`RAG_production_app/`)

*   **Description:** This is a Retrieval-Augmented Generation (RAG) application built with FastAPI and Inngest.
*   **Key Technologies:** Python, FastAPI, Inngest.

### Reddit Scraping Pipeline (`Reddit_scraping_pipeline/`)

*   **Description:** This project contains a series of Jupyter notebooks and a Django app that demonstrate how to build an AI-powered pipeline for discovering and analyzing Reddit communities based on given topics.
*   **Key Technologies:** Python, LangChain, LangGraph, Django, Celery, BrightData SERP, Google Gemini.

### Simple AI Agent (`simple_AI_agent/`)

*   **Description:** DataGen Agent is a sophisticated, command-line-driven AI agent designed to generate realistic, synthetic user data based on natural language instructions. Built with Python, LangChain, and OpenAI, it provides a conversational interface for creating and managing sample datasets effortlessly.
*   **Key Technologies:** Python, LangChain, LangGraph, OpenAI.

## Getting Started

Each project directory contains its own `README.md` file (or relevant setup information in its code) with specific instructions for setup, dependencies, and usage. Please refer to the individual project directories for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## Disclaimer

These projects are for educational and experimental purposes only. They are not intended for production use without further development and testing.

## Contact

If you have any questions, feel free to reach out to me at [dim.pashev@gmail.com](mailto:dim.pashev@gmail.com).

## Acknowledgments

Special thanks to the open-source community for the amazing tools and libraries that made these projects possible.
