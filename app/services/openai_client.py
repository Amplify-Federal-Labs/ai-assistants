import os
from typing import Dict, Any, List
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from openai.types.chat.chat_completion_system_message_param import ChatCompletionSystemMessageParam
from openai.types.chat.chat_completion_user_message_param import ChatCompletionUserMessageParam
from openai.types.chat.chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam

class OpenAIClient:
    """A wrapper around OpenAI's client that maintains configuration and message formatting."""
    
    DEFAULT_MODEL = "gpt-3.5-turbo"
    DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."
    
    def __init__(self, 
                 system_prompt: str | None = None, 
                 api_key: str | None = None, 
                 model: str | None = None):
        """Initialize an OpenAI client instance.
        
        Args:
            system_prompt (str | None, optional): The system prompt that defines the assistant's behavior.
                Defaults to DEFAULT_SYSTEM_PROMPT.
            api_key (str | None, optional): The OpenAI API key. If not provided,
                it will be read from the OPENAI_API_KEY environment variable.
            model (str | None, optional): The OpenAI model to use. Defaults to DEFAULT_MODEL.
        
        Raises:
            ValueError: If no API key is provided and OPENAI_API_KEY environment variable is not set.
        """
        # Use provided api_key or fall back to environment variable
        final_api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not final_api_key:
            raise ValueError(
                "OpenAI API key must be provided either through the api_key parameter "
                "or the OPENAI_API_KEY environment variable"
            )

        self._system_prompt = system_prompt or self.DEFAULT_SYSTEM_PROMPT
        self._model = model or self.DEFAULT_MODEL
        
        system_message: ChatCompletionSystemMessageParam = {
            "role": "system", 
            "content": self._system_prompt
        }
        self._messages: List[ChatCompletionMessageParam] = [system_message]
        
        self._client = OpenAI(api_key=final_api_key)
    
    @property
    def client(self) -> OpenAI:
        """Get the underlying OpenAI client instance."""
        return self._client
    
    @property
    def messages(self) -> List[ChatCompletionMessageParam]:
        """Get the current message history."""
        return self._messages.copy()
        
    def send_message(self, message: str) -> str:
        """Send a message to OpenAI's chat completion API and get the response.
        
        Args:
            message (str): The message content to send.
        
        Returns:
            str: The assistant's response message content.
            
        Raises:
            ValueError: If the API returns no content or None.
        """
        # Create user message and prepare API request
        user_message: ChatCompletionUserMessageParam = {"role": "user", "content": message}
        api_messages = self.messages  # Get current history
        api_messages.append(user_message)  # Add user message for API call
        
        # Make API call with messages as they were before this interaction
        response = self._client.chat.completions.create(
            messages=api_messages,
            model=self._model
        )
        
        # Extract assistant's response
        assistant_message = response.choices[0].message
        assistant_content = assistant_message.content
        
        if assistant_content is None:
            raise ValueError("OpenAI API returned no content")
        
        # Update message history with both user message and assistant's response
        self._messages.append(user_message)
        assistant_response: ChatCompletionAssistantMessageParam = {
            "role": "assistant", 
            "content": assistant_content
        }
        self._messages.append(assistant_response)
        
        return assistant_content