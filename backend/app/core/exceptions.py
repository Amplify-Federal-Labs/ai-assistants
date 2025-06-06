"""Custom exceptions for the application."""


class AdaConverterError(Exception):
    """Base exception for Ada converter related errors."""
    pass


class FileUploadError(Exception):
    """Exception raised for file upload related errors."""
    pass


class ConfigurationError(Exception):
    """Exception raised for configuration related errors."""
    pass