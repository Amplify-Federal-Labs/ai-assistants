import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application configuration settings."""
    
    def __init__(self):
        self.openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
        self.openai_model: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        
        # API Settings
        self.api_host: str = os.getenv("API_HOST", "127.0.0.1")
        self.api_port: int = int(os.getenv("API_PORT", "8000"))
        self.debug: bool = os.getenv("DEBUG", "True").lower() == "true"
        
        # File upload settings
        self.max_file_size: int = int(os.getenv("MAX_FILE_SIZE", "1048576"))  # 1MB default
        self.allowed_extensions: set = {".ada", ".adb", ".ads"}
    
    def validate(self) -> None:
        """Validate required configuration settings."""
        if not self.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable is required"
            )


# Global settings instance
settings = Settings()