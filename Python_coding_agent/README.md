# Python Coding Agent

A command-line tool that leverages Google's Gemini AI to act as an intelligent coding agent. It can perform file operations (list, read, write) and execute Python scripts based on natural language prompts.

## Features

- List files and directories
- Read file contents
- Write to files (create or update)
- Run Python files with optional arguments
- Built on Google Gemini 2.0 Flash API for smart function calling

## Installation

Requires Python >= 3.13.

1. Clone the repository:
   ```bash
   git clone https://github.com/dimipash/AI-Python-projects.git
   cd Python_coding_agent
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Set up environment:
   - Create a `.env` file in the project root
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`

## Usage

Run the agent with a prompt:

```bash
python main.py "List the files in the current directory"
```

For verbose output showing token usage:

```bash
python main.py "Read the main.py file" --verbose
```

## Included Example

The `calculator/` subdirectory contains a simple calculator implementation with unit tests, demonstrating basic Python project structure and testing practices.

## License

MIT
