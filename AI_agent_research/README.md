# AI Research Agent

This is a Python application that acts as an AI research assistant. It utilizes large language models (LLMs) and various tools to perform research on a given topic and generate a structured output.

## Features

- **Research Capabilities:** Uses DuckDuckGo and Wikipedia to gather information.
- **LLM Integration:** Supports different LLMs (OpenAI and Anthropic) for generating research summaries.
- **Structured Output:** Provides research results in a structured format including topic, summary, sources, and tools used.
- **Output Saving:** Can save the research output to a text file.

## Requirements

- Python 3.7+
- Libraries listed in `requirements.txt`

## Installation

1. Clone this repository


2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your API keys for the LLMs you intend to use:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```
   *(Note: You only need to provide keys for the models you plan to use.)*

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. The application will prompt you to enter the LLM model name and your research query.

3. The agent will then perform the research using the available tools and display the structured output.

4. The output will also be saved to `research_output.txt`.

## Project Structure

- `main.py`: The main script that orchestrates the research agent.
- `tools.py`: Contains the definitions for the tools used by the agent (DuckDuckGo search, Wikipedia search, file saving).
- `requirements.txt`: Lists the Python dependencies.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.
- `research_output.txt`: Default file where research output is saved.
