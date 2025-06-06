# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Claude Code Instructions

### Development Approach
- **Pairing Partner**: Act as a TDD pairing partner following red-green-refactor cycle
- **Explicit Consent**: ALWAYS ask for explicit consent before making changes
- **Test-Driven Development**: Every feature starts with a failing test, minimal implementation, then refactor
- **Concise Communication**: Keep responses short and focused (fewer than 4 lines unless detail is requested)
- **Task Management**: Use TodoWrite/TodoRead tools frequently to track progress and give user visibility

### Coding Standards
- Use type hints for all function signatures
- Follow PEP 8 style guidelines
- Write comprehensive docstrings for classes and methods
- NO comments in code unless explicitly requested
- Prefer editing existing files over creating new ones
- Never commit changes unless explicitly asked by user

### Project Structure
```
ai-assistants/
├── app/                            # Main application
│   ├── api/v1/endpoints/          # Versioned API endpoints
│   ├── core/                      # Configuration and utilities
│   ├── services/                  # Business logic
│   └── main.py                    # Flask app factory
├── tests/                         # Mirror app/ structure
│   ├── conftest.py               # Shared fixtures
│   ├── api/v1/endpoints/         # API tests
│   ├── core/                     # Core module tests
│   └── services/                 # Service tests
└── pyproject.toml                # Project configuration
```

### Testing Practices
- Use shared fixtures from `tests/conftest.py`
- Mock external dependencies (OpenAI API calls)
- Test files mirror the `app/` directory structure
- Run tests after every change: `uv run pytest`
- Can run tests by module: `uv run pytest tests/core/`

## Commands

### Development Setup
```bash
uv pip install -e .
```

### Running Tests
```bash
uv run pytest
```

### Running the API Server
```bash
PYTHONPATH=. uv run python app/main.py
```

### Running Tests by Module
```bash
uv run pytest tests/core/        # Core module tests
uv run pytest tests/api/         # API tests
uv run pytest tests/services/    # Service tests
```

## Architecture

This is a Python-based REST API for Ada to Python code conversion with the following components:

### Core Components
- **app/main.py**: Flask app factory with configuration management
- **app/services/openai_client.py**: `OpenAIClient` class - core wrapper around OpenAI API
- **app/services/ada_converter.py**: `AdaConverter` class - specialized service for converting Ada code to Python
- **app/api/v1/endpoints/convert.py**: REST API endpoint for file upload and conversion
- **app/core/config.py**: Centralized configuration management with environment variable support

### Key Architecture Patterns
- **Separation of Concerns**: Clear distinction between API, business logic, and configuration
- **Versioned APIs**: `/api/v1/convert` for new integrations, `/convert` for backward compatibility
- **Configuration Management**: Centralized settings with validation in `app/core/config.py`
- **Service Layer**: Business logic isolated in `app/services/`
- **Test Structure**: Tests mirror application structure for maintainability

### API Endpoints
- **POST /convert**: Legacy endpoint for backward compatibility
- **POST /api/v1/convert**: Versioned endpoint for file upload and Ada to Python conversion

### API Key Configuration
The application expects `OPENAI_API_KEY` environment variable or `.env` file. Configuration is managed through `app/core/config.py` with validation.