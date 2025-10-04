# Reddit Scraping Pipeline

This project contains a series of Jupyter notebooks and a Django app that demonstrate how to build an AI-powered pipeline for discovering and analyzing Reddit communities based on given topics. It utilizes LangChain, LangGraph, Django, Celery, and external APIs like BrightData SERP and Google Gemini to create an intelligent agent that searches the internet for relevant Reddit subreddits.

## Features

- **Web Search Integration**: Uses BrightData SERP API for reliable Google search capabilities.
- **Large Language Model**: Integrates Google Gemini LLM for natural language processing and reasoning.
- **Agent Framework**: Employs LangGraph to build ReAct agents for automated, step-by-step tasks.
- **Structured Data Handling**: Uses Pydantic models for structured JSON outputs representing Reddit communities.
- **Tool Calling**: Demonstrates LangChain's tool-calling capabilities for extending LLM functionality.
- **Environment Management**: Secure handling of API keys via environment variables.
- **Django App**: Includes a Django project for web-based or backend integration.
- **Task Queue**: Celery is included for background task processing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dimipash/AI-Python-projects.git
   cd Reddit_scraping_pipeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If you encounter errors related to `pydantic-core` or other dependencies, ensure you have a recent version of `pip` and required build tools:
   ```bash
   pip install --upgrade pip setuptools wheel
   sudo apt-get install build-essential
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys:
     ```
     GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
     BRIGHT_DATA_SERP_API_KEY=your_bright_data_serp_api_key
     ```

## Usage

Open and run the notebooks in sequential order in Jupyter:

1. `notebooks/1-hello-world.ipynb` - Basic setup and hello world
2. `notebooks/2-load-env-vars.ipynb` - Loading environment variables securely
3. `notebooks/3-serp-api-langchain.ipynb` - Integrating SERP API with LangChain
4. `notebooks/4-google-gemini-llm-langchain.ipynb` - Setting up Google Gemini LLM
5. `notebooks/5-structured-output-with-langchain-pydantic.ipynb` - Structured outputs with Pydantic
6. `notebooks/6-llm-tool-calling.ipynb` - Tool calling with LangChain
7. `notebooks/7-llm-tool-calling-easy.ipynb` - Simplified tool calling examples
8. `notebooks/8-searching-reddit-communites-by-topic.ipynb` - Final pipeline: Search for Reddit communities by topic
9. `notebooks/9-scraping-subreddit-threads.ipynb` - Example: Scraping subreddit threads
10. `notebooks/10-django-hello-world.ipynb` - Django hello world example

In the final notebook, you can modify the input topics and run the agent to get a list of relevant Reddit communities with details like member counts.

### Django App

This project includes a Django app (in `src/`). To run the Django development server:

```bash
cd src
python manage.py migrate
python manage.py runserver
```

Celery is included for background task processing. To start a Celery worker:

```bash
celery -A dlphome worker --loglevel=info
```

## Requirements

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- API keys for Google Gemini and BrightData SERP

See `requirements.txt` for a complete list of Python dependencies. Notable packages:

- Django, Celery, dj-database-url, psycopg[binary]
- jupyter, python-dotenv
- langchain, langchain-community, langchain-brightdata, langchain[google-genai], langgraph

## Project Structure

```
Reddit_scraping_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── dlphome/  # Django app
│   └── manage.py
└── notebooks/
   ├── 1-hello-world.ipynb
   ├── 2-load-env-vars.ipynb
   ├── 3-serp-api-langchain.ipynb
   ├── 4-google-gemini-llm-langchain.ipynb
   ├── 5-structured-output-with-langchain-pydantic.ipynb
   ├── 6-llm-tool-calling.ipynb
   ├── 7-llm-tool-calling-easy.ipynb
   ├── 8-searching-reddit-communites-by-topic.ipynb
   ├── 9-scraping-subreddit-threads.ipynb
   └── 10-django-hello-world.ipynb
```

## Technologies Used

- LangChain: For building LLM-powered applications
- LangGraph: For creating agent workflows
- LangChain BrightData: For integration with BrightData SERP
- Google GenAI: For access to Gemini models
- Pydantic: For data validation and structured outputs
- Python-dotenv: For environment variable management
- Jupyter: For interactive notebook development
- Django: For web application and backend
- Celery: For background task processing

## Contributing

This is an educational project demonstrating AI pipeline techniques. Feel free to fork and experiment with the code. If you encounter issues with dependency installation, please check your Python version and ensure all build tools are installed.

## License

This project is part of a personal learning repository and is available as-is for educational purposes.
