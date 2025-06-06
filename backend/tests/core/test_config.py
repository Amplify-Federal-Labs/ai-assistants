"""Tests for configuration module."""

import pytest
import os
from unittest.mock import patch
from app.core.config import Settings


def test_settings_default_values():
    """Test that settings have correct default values."""
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-key'}, clear=True):
        settings = Settings()
        
        assert settings.openai_model == "gpt-3.5-turbo"
        assert settings.api_host == "127.0.0.1"
        assert settings.api_port == 5000
        assert settings.debug is True
        assert settings.max_file_size == 1048576
        assert settings.allowed_extensions == {".ada", ".adb", ".ads"}


def test_settings_from_environment():
    """Test that settings are loaded from environment variables."""
    env_vars = {
        'OPENAI_API_KEY': 'test-key-env',
        'OPENAI_MODEL': 'gpt-4',
        'API_HOST': '0.0.0.0',
        'API_PORT': '8080',
        'DEBUG': 'false',
        'MAX_FILE_SIZE': '2097152'
    }
    
    with patch.dict(os.environ, env_vars, clear=True):
        settings = Settings()
        
        assert settings.openai_api_key == 'test-key-env'
        assert settings.openai_model == 'gpt-4'
        assert settings.api_host == '0.0.0.0'
        assert settings.api_port == 8080
        assert settings.debug is False
        assert settings.max_file_size == 2097152


def test_settings_validation_missing_api_key():
    """Test that validation fails when OpenAI API key is missing."""
    with patch.dict(os.environ, {}, clear=True):
        settings = Settings()
        
        with pytest.raises(ValueError, match="OPENAI_API_KEY environment variable is required"):
            settings.validate()


def test_settings_validation_success():
    """Test that validation passes with required settings."""
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-key'}, clear=True):
        settings = Settings()
        
        # Should not raise an exception
        settings.validate()