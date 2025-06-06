# Ada to Python Converter

Full-stack web application for converting Ada code to Python with explanations and unit tests. Built with React TypeScript frontend and Flask Python backend, following Test-Driven Development practices.

## Setup

### Prerequisites

- Python 3.11 or higher
- `uv` package manager
- Node.js 18+ and npm
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-assistants
```

2. Install backend dependencies:
```bash
cd backend
uv pip install -e .
cd ..
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
cd ..
```

### Configuration

The application requires an OpenAI API key to function. You can configure it in two ways:

1. **Environment Variable (Recommended for Production)**
   
   Set the `OPENAI_API_KEY` environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

   For permanent configuration, add it to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.).

2. **Local Development with .env file**
   
   Create a `.env` file in the project root:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```
   
   Make sure to add `.env` to your `.gitignore`:
   ```bash
   echo ".env" >> .gitignore
   ```


### Security Considerations

- Never commit API keys to version control
- Use environment variables or secure parameter stores in production
- For CI/CD pipelines, use secret management features (e.g., GitHub Secrets)

## Development

### Running the Application

Start both the backend API and frontend development server:

**Terminal 1 - Backend API (Port 8000):**
```bash
cd backend
PYTHONPATH=. uv run python app/main.py
```

**Terminal 2 - Frontend Dev Server (Port 5173):**
```bash
cd frontend
npm run dev
```

Access the application at **http://localhost:5173**

### Features

- **File Upload**: Upload Ada files (.ada, .adb) with validation
- **Code Conversion**: AI-powered conversion from Ada to Python
- **Explanations**: Detailed logic explanations for converted code
- **Unit Tests**: Automatically generated Python unit tests
- **Copy Functionality**: Copy converted code and tests to clipboard
- **Error Handling**: User-friendly error messages and validation

### Testing

**Backend Tests:**
```bash
cd backend
uv run python -m pytest                    # Run all backend tests
uv run python -m pytest tests/core/        # Core module tests
uv run python -m pytest tests/api/         # API tests
uv run python -m pytest tests/services/    # Service tests
```

**Frontend Tests:**
```bash
cd frontend
npm test                                    # Run all frontend tests
npm run test:ui                            # Run tests with UI
```

### Architecture

```
ai-assistants/
├── backend/                 # Flask API Backend
│   ├── app/                # Main application
│   │   ├── api/v1/endpoints/ # REST API endpoints
│   │   ├── core/           # Configuration & utilities
│   │   ├── services/       # Business logic
│   │   └── main.py        # Flask app with CORS
│   ├── tests/             # Backend test suite
│   ├── cli/               # Command line interface
│   └── pyproject.toml     # Backend dependencies
├── frontend/               # React TypeScript Frontend  
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── services/      # API client
│   │   └── types/         # TypeScript interfaces
│   └── vite.config.ts     # Dev server with API proxy
└── [docs]                 # README.md, CLAUDE.md, .gitignore
```

### Technology Stack

**Backend:**
- Flask (Python web framework)
- OpenAI API (GPT-4 for code conversion)
- Flask-CORS (Cross-origin resource sharing)
- Pytest (Testing framework)

**Frontend:**
- React 18 (UI framework)
- TypeScript (Type safety)
- Vite (Build tool & dev server)
- TanStack Query (API state management)
- React Hook Form (Form handling)
- Vitest + React Testing Library (Testing)

## License

[Add your license here]