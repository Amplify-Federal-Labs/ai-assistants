"""Tests for custom exceptions."""

import pytest
from app.core.exceptions import AdaConverterError, FileUploadError, ConfigurationError


def test_ada_converter_error():
    """Test AdaConverterError exception."""
    error_msg = "Ada conversion failed"
    
    with pytest.raises(AdaConverterError, match=error_msg):
        raise AdaConverterError(error_msg)


def test_file_upload_error():
    """Test FileUploadError exception."""
    error_msg = "File upload failed"
    
    with pytest.raises(FileUploadError, match=error_msg):
        raise FileUploadError(error_msg)


def test_configuration_error():
    """Test ConfigurationError exception."""
    error_msg = "Configuration is invalid"
    
    with pytest.raises(ConfigurationError, match=error_msg):
        raise ConfigurationError(error_msg)


def test_exceptions_are_subclass_of_exception():
    """Test that all custom exceptions inherit from Exception."""
    assert issubclass(AdaConverterError, Exception)
    assert issubclass(FileUploadError, Exception)
    assert issubclass(ConfigurationError, Exception)