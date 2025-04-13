# AI Notes MCP Server for Claude Desktop App

A custom Model Context Protocol (MCP) server implementation for managing sticky notes through the Claude Desktop App interface.

## Features

- 📝 Persistent note storage in local text file
- 🔄 Real-time synchronization with Claude Desktop App
- 🛠️ MCP Tools for note management:
  - Add new notes
  - Read full history
  - Get latest note
  - Generate AI summary prompts

## Installation

1. Ensure Python 3.10+ is installed
2. Install dependencies:
```bash
uv install
```

## Usage

```bash
uv main.py
```

The server will start on port 8000 and create:
- `notes.txt`: Auto-created notes storage file
- `uv.lock`: Dependency lock file

## API Reference

### Tools
```python
@mcp.tool()
def add_note(message: str) -> str
```
**Parameters:**
- `message`: Note content (1-500 characters)

**Returns:** Confirmation message

```python
@mcp.tool() 
def read_notes() -> str
```
**Returns:** All notes concatenated with newlines

### Resources
```python
@mcp.resource("notes://latest")
def get_latest_note() -> str
```
**Returns:** Most recent note entry

### Prompts
```python
@mcp.prompt()
def note_summary_prompt() -> str
```
**Returns:** Pre-formatted prompt for AI summarization

## Configuration

Edit `pyproject.toml` for:
- Port configuration
- Timeout settings
- Logging levels

## Development

```bash
# Run with hot reload
uv main.py --reload

# Run tests
uv test
```

## Security

- Notes stored locally in plain text
- No external network access required
- File permissions match user account

## License

MIT License - See [LICENSE](LICENSE) for details
