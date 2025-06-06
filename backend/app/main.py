from flask import Flask
from flask_cors import CORS
from app.core.config import settings
from app.api.v1 import api_v1


def create_app() -> Flask:
    """Create and configure the Flask application."""
    # Validate configuration
    settings.validate()
    
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = settings.max_file_size
    
    # Enable CORS for frontend
    cors_origins = [
        "http://localhost:5173",  # Local development
        "http://localhost:3000",  # Alternative local port
        "https://*.netlify.app",  # Netlify deployments
        # Add your production frontend URL here
    ]
    
    CORS(app, 
         origins=cors_origins if not settings.debug else "*",
         methods=['GET', 'POST', 'OPTIONS'],
         allow_headers=['Content-Type', 'Authorization'],
         supports_credentials=False)
    
    # Register blueprints
    app.register_blueprint(api_v1)
    
    
    return app


def main():
    """Run the Flask application."""
    app = create_app()
    app.run(
        host=settings.api_host,
        port=settings.api_port,
        debug=settings.debug
    )


if __name__ == '__main__':
    main()