# ChatGPT Apps SDK

This project is a Python-based web service that demonstrates the use of the FastMCP library to create a tool-use MCP (Multi-turn Conversation Protocol) application. The project also includes a FastAPI web application that exposes both regular API endpoints and the MCP application.

## Running the Project

To run the applications, you can use the scripts defined in the `rav.yaml` file.

### Running the FastAPI Application

To run the main FastAPI application, which includes the MCP application, use the following command:

```bash
rav dev
```

This will start the application on `http://0.0.0.0:8123`. The API documentation will be available at `http://0.0.0.0:8123/docs`.

### Running the Standalone MCP Application

To run the standalone MCP application, use the following command:

```bash
rav mcp_app_only
```

This will start the MCP application on `http://localhost:8123`.
