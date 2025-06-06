"""Shared test fixtures and configuration for the test suite."""

import pytest
from unittest.mock import patch
from io import BytesIO


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client to avoid API calls during testing."""
    with patch('app.services.ada_converter.OpenAIClient') as mock:
        yield mock


@pytest.fixture
def sample_ada_code():
    """Sample Ada code for testing."""
    return """
    procedure Hello is
    begin
        Put_Line("Hello, World!");
    end Hello;
    """


@pytest.fixture
def sample_converter_response():
    """Sample response from Ada converter."""
    return """# Logic
Simple Ada procedure that prints Hello, World!
# Unit Test
def test_hello():
    assert hello() == 'Hello, World!'
# Python Code
def hello():
    return 'Hello, World!'"""


@pytest.fixture
def ada_file_upload(sample_ada_code):
    """Create a file-like object for testing file uploads."""
    return BytesIO(sample_ada_code.encode('utf-8'))


@pytest.fixture
def flask_test_client():
    """Create a Flask test client for API testing."""
    with patch('app.services.ada_converter.OpenAIClient'):
        from app.main import create_app
        app = create_app()
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client