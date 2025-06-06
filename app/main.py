from flask import Flask
from app.core.config import settings
from app.api.v1 import api_v1


def create_app() -> Flask:
    """Create and configure the Flask application."""
    # Validate configuration
    settings.validate()
    
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = settings.max_file_size
    
    # Register blueprints
    app.register_blueprint(api_v1)
    
    # Legacy route for backward compatibility
    from app.api.v1.endpoints.convert import convert_ada_file
    app.add_url_rule('/convert', 'legacy_convert', convert_ada_file, methods=['POST'])
    
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