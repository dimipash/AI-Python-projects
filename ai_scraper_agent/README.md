# AI Scraper Agent

This project is an AI-powered web scraper agent that extracts the latest posts from an Instagram page. It leverages the `browser-use` library for browser automation and `langchain-anthropic` for interacting with Anthropic's models to achieve this task.

## Features

- Scrapes the latest posts from a specified Instagram profile.
- Uses an AI agent to navigate and extract relevant information from the webpage.
- Outputs the scraped data in JSON format.

## Dependencies

- `langchain-anthropic`
- `browser-use`
- `python-dotenv`
- `pydantic`
- `asyncio`
- `playwright`

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables**:
   - Ensure you have an Anthropic API key set in your environment variables as required by `langchain-anthropic`.
   - The script uses `python-dotenv` to load environment variables from a `.env` file if present.

## How to Run

To run the scraper, execute the `main.py` script:

```bash
python main.py
```

This script will:

1. Open a browser and navigate to the specified Instagram profile (currently set to `@thepashi`).
2. Instruct the AI agent to extract the 5 latest posts.
3. Print the extracted post data in JSON format to the console.
4. Close the browser.

## Configuration

- **Instagram Profile**: The target Instagram profile is currently hardcoded in `main.py` in the `initial_actions` list. You can modify this to scrape different profiles.
- **Number of Posts**: The task is set to retrieve the 5 latest posts. This can be adjusted in the agent's task description in `main.py`.
- **Browser**: The browser configuration in `main.py` is set to use Google Chrome. Ensure the `chrome_instance_path` is correctly configured for your system.


