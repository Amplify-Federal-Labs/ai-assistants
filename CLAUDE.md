# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development Setup
```bash
uv pip install -e .
```

### Running Tests
```bash
uv run pytest
```

### Running the Application
```bash
python main.py
```

## Architecture

This is a Python-based OpenAI assistant chatbot with the following key components:

### Core Components
- **main.py**: CLI entry point using Click library for interactive chat interface
- **src/api.py**: `OpenAIClient` class - core wrapper around OpenAI API that maintains conversation history and configuration
- **src/chatbot.py**: `Chatbot` class - simple wrapper around OpenAIClient with default system prompt
- **src/ada_converter.py**: `AdaConverter` class - specialized chatbot for converting Ada code to Python

### Key Architecture Patterns
- The `OpenAIClient` class maintains conversation state by tracking message history in `_messages` list
- All OpenAI interactions go through the `OpenAIClient.send_message()` method which automatically appends user and assistant messages to history
- Configuration is handled through environment variables (`OPENAI_API_KEY`) with optional `.env` file support
- Each specialized chatbot (like `AdaConverter`) creates its own `OpenAIClient` instance with domain-specific system prompts

### API Key Configuration
The application expects `OPENAI_API_KEY` environment variable or `.env` file. API key can also be passed programmatically to `OpenAIClient` constructor.

### Testing
Tests use pytest with mocking of OpenAI API calls. Test files mirror the src/ structure.