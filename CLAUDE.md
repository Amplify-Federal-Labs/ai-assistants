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
├── backend/                        # Flask API Backend
│   ├── app/                       # Main application
│   │   ├── api/v1/endpoints/     # Versioned API endpoints
│   │   ├── core/                 # Configuration and utilities
│   │   ├── services/             # Business logic
│   │   └── main.py               # Flask app factory with CORS
│   ├── tests/                    # Backend tests (mirror app/ structure)
│   │   ├── conftest.py          # Shared fixtures
│   │   ├── api/v1/endpoints/    # API tests
│   │   ├── core/                # Core module tests
│   │   └── services/            # Service tests
│   ├── cli/                     # Command line interface
│   └── pyproject.toml           # Backend configuration
├── frontend/                       # React TypeScript Frontend
│   ├── src/
│   │   ├── components/            # React components (FileUpload, CodeDisplay)
│   │   ├── services/              # API client services
│   │   ├── types/                 # TypeScript interfaces
│   │   ├── App.tsx               # Main application component
│   │   └── main.tsx              # React entry point
│   ├── package.json              # Frontend dependencies
│   ├── vite.config.ts            # Vite config with API proxy
│   └── vitest.config.ts          # Frontend testing config
└── [docs and config files]        # README.md, CLAUDE.md, .gitignore
```

### Testing Practices
**Backend Testing:**
- Use shared fixtures from `backend/tests/conftest.py`
- Mock external dependencies (OpenAI API calls)
- Test files mirror the `backend/app/` directory structure
- Run tests after every change: `cd backend && uv run python -m pytest`
- Can run tests by module: `cd backend && uv run python -m pytest tests/core/`

**Frontend Testing:**
- TDD approach with Vitest + React Testing Library
- Tests located alongside components in `frontend/src/`
- Mock API calls and external dependencies
- Run tests: `npm test` (single run) or `npm run test:ui` (watch mode)
- Test structure mirrors component structure

## Commands

### Backend Setup & Development
```bash
cd backend

# Install dependencies
uv pip install -e .

# Run backend tests
uv run python -m pytest

# Run backend server (localhost:8000)
PYTHONPATH=. uv run python app/main.py

# Run tests by module
uv run python -m pytest tests/core/        # Core module tests
uv run python -m pytest tests/api/         # API tests
uv run python -m pytest tests/services/    # Service tests
```

**Note:** Backend runs on port 8000 to avoid conflicts with macOS AirPlay Receiver (port 5000).

### Frontend Setup & Development
```bash
cd frontend

# Install dependencies
npm install

# Run frontend tests
npm test

# Run frontend dev server (localhost:5173)
npm run dev

# Build for production
npm run build
```

### Full Stack Development
```bash
# Terminal 1: Backend API
cd backend && PYTHONPATH=. uv run python app/main.py

# Terminal 2: Frontend Dev Server
cd frontend && npm run dev

# Access application at http://localhost:5173
# API requests automatically proxy to localhost:8000
```

## Architecture

Full-stack application with React TypeScript frontend and Flask Python backend for Ada to Python code conversion.

### Backend Components
- **backend/app/main.py**: Flask app factory with CORS configuration for frontend integration
- **backend/app/services/openai_client.py**: `OpenAIClient` class - core wrapper around OpenAI API
- **backend/app/services/ada_converter.py**: `AdaConverter` class - specialized service for converting Ada code to Python
- **backend/app/api/v1/endpoints/convert.py**: REST API endpoint for file upload and conversion
- **backend/app/core/config.py**: Centralized configuration management with environment variable support

### Frontend Components
- **frontend/src/App.tsx**: Main application with TanStack Query for state management
- **frontend/src/components/FileUpload.tsx**: File upload with Ada file validation (.ada, .adb)
- **frontend/src/components/CodeDisplay.tsx**: Code display with syntax highlighting and copy functionality
- **frontend/src/services/api.ts**: API client for backend communication
- **frontend/src/types/api.ts**: TypeScript interfaces for API contracts

### Key Architecture Patterns
- **Full Stack Separation**: Clear separation between React frontend and Flask backend
- **CORS Integration**: Backend configured to serve frontend requests from localhost:5173
- **API Proxy**: Vite dev server proxies `/api` requests to Flask backend
- **Versioned APIs**: Clean `/api/v1/convert` endpoint (legacy `/convert` removed)
- **TDD Approach**: Both frontend and backend developed with comprehensive test coverage
- **Configuration Management**: Centralized settings with validation in `app/core/config.py`
- **Service Layer**: Business logic isolated in `app/services/`
- **Component Testing**: Frontend components tested with React Testing Library + Vitest

### API Endpoints
- **POST /api/v1/convert**: File upload and Ada to Python conversion

### Development Workflow
1. **Backend**: Flask API serves conversion logic (port 8000)
2. **Frontend**: React dev server with hot reload (port 5173)
3. **Integration**: Vite proxies API calls from frontend to backend
4. **Testing**: Separate test suites for frontend and backend components

**Port Configuration:**
- Backend uses port 8000 to avoid macOS AirPlay Receiver conflicts (port 5000)
- Frontend proxy automatically forwards `/api` requests to `localhost:8000`

### API Key Configuration
The application expects `OPENAI_API_KEY` environment variable or `.env` file. Configuration is managed through `backend/app/core/config.py` with validation.