import os
from unittest.mock import Mock, patch, call, ANY
import pytest
from src.api import OpenAIClient
from openai import OpenAI

def test_openai_client_initialization_with_env_var(monkeypatch):
    # Given
    monkeypatch.setenv("OPENAI_API_KEY", "test-key-from-env")
    system_prompt = "You are a helpful assistant."
    
    # When
    client = OpenAIClient(system_prompt=system_prompt)
    
    # Then
    assert isinstance(client.client, OpenAI)
    assert client._model == OpenAIClient.DEFAULT_MODEL

def test_openai_client_initialization_with_explicit_key():
    # Given
    system_prompt = "You are a helpful assistant."
    
    # When
    client = OpenAIClient(system_prompt=system_prompt, api_key="test-key-explicit")
    
    # Then
    assert isinstance(client.client, OpenAI)
    assert client._model == OpenAIClient.DEFAULT_MODEL

def test_openai_client_initialization_with_custom_model():
    # Given
    system_prompt = "You are a helpful assistant."
    custom_model = "gpt-4"
    
    # When
    client = OpenAIClient(system_prompt=system_prompt, api_key="test-key", model=custom_model)
    
    # Then
    assert isinstance(client.client, OpenAI)
    assert client._model == custom_model

def test_openai_client_without_key(monkeypatch):
    # Given
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    system_prompt = "You are a helpful assistant."
    
    # Then
    with pytest.raises(ValueError) as exc_info:
        OpenAIClient(system_prompt=system_prompt)
    
    assert "OpenAI API key must be provided" in str(exc_info.value)

def test_openai_client_initialization_with_default_system_prompt():
    # Given
    # When
    client = OpenAIClient(api_key="test-key")
    
    # Then
    assert isinstance(client.client, OpenAI)
    assert client._model == OpenAIClient.DEFAULT_MODEL
    assert client._system_prompt == OpenAIClient.DEFAULT_SYSTEM_PROMPT

def test_send_message(monkeypatch):
    # Given
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    system_prompt = "You are a helpful assistant."
    message = "Hello, how are you?"
    expected_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]
    
    with patch('src.api.OpenAI') as mock_openai_class:
        mock_openai = Mock()
        mock_openai_class.return_value = mock_openai
        mock_chat = Mock()
        mock_openai.chat = mock_chat
        mock_completions = Mock()
        mock_chat.completions = mock_completions
        
        # Create a mock message with content attribute
        mock_message = Mock()
        mock_message.content = "Hi! How can I help?"
        mock_message.role = "assistant"
        
        mock_response = Mock()
        mock_response.choices = [Mock(message=mock_message)]
        mock_completions.create.return_value = mock_response
        
        # When
        client = OpenAIClient(system_prompt=system_prompt)
        response = client.send_message(message)
        
        # Then
        assert response == "Hi! How can I help?"
        
        # Verify that the API was called with the right messages
        mock_completions.create.assert_called_once_with(
            messages=expected_messages,
            model=OpenAIClient.DEFAULT_MODEL
        )

def test_message_history():
    # Given
    system_prompt = "You are a helpful assistant."
    client = OpenAIClient(system_prompt=system_prompt, api_key="test-key")
    
    # Then
    assert client.messages == [{"role": "system", "content": system_prompt}]
    
    # When sending a message
    with patch.object(client._client.chat.completions, 'create') as mock_create:
        # Create a mock message with content attribute
        mock_message = Mock()
        mock_message.content = "Hello!"
        mock_message.role = "assistant"
        
        mock_response = Mock()
        mock_response.choices = [Mock(message=mock_message)]
        mock_create.return_value = mock_response
        
        # When
        client.send_message("Hi!")
        
        # Then
        assert client.messages == [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Hi!"},
            {"role": "assistant", "content": "Hello!"}
        ]
