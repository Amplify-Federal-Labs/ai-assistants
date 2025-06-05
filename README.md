# AI Assistants

Python-based assistants using OpenAI's API.

## Setup

### Prerequisites

- Python 3.11 or higher
- `uv` package manager

### Installation

1. Clone the repository:
```bash
git clone git@github.com:Amplify-Federal-Labs/ai-assistants.git
cd ai-assistants
```

2. Install dependencies:

No need to install dependencies. uv will automatically install dependencies when run.

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

3. **Programmatic Configuration**
   
   You can also provide the API key directly when creating the client:
   ```python
   from src.api import create_openai_client
   
   client = create_openai_client(api_key="your-api-key-here")
   ```

### Security Considerations

- Never commit API keys to version control
- Use environment variables or secure parameter stores in production
- For CI/CD pipelines, use secret management features (e.g., GitHub Secrets)

## Development

### Running Tests

```bash
uv run pytest
```

## License

[Add your license here]