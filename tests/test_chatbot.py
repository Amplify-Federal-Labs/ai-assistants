from unittest.mock import Mock, patch, call, ANY
import pytest
from src.chatbot import Chatbot
from src.api import OpenAIClient
from openai import OpenAI

def test_chatbot_initialization_with_env_var(monkeypatch):
    # Given
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    
    # When
    chatbot = Chatbot()
    
    # Then
    assert isinstance(chatbot.client, OpenAIClient)
    assert isinstance(chatbot.client.client, OpenAI)

def test_chatbot_sends_system_prompt(monkeypatch):
    # Given
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    message = "Hi there!"
    expected_system_prompt = "You are a helpful assistant that provides clear and concise answers."
    expected_messages = [
        {"role": "system", "content": expected_system_prompt},
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
        mock_message.content = "Hello!"
        mock_message.role = "assistant"
        
        mock_response = Mock()
        mock_response.choices = [Mock(message=mock_message)]
        mock_completions.create.return_value = mock_response
        
        # When
        chatbot = Chatbot()
        response = chatbot.send_message(message)
        
        # Then
        assert response == "Hello!"
        
        # Verify that the API was called with the right messages
        mock_completions.create.assert_called_once_with(
            messages=expected_messages,
            model="gpt-3.5-turbo"
        )
