from .api import OpenAIClient

class Chatbot:
    # Default system prompt that defines the chatbot's behavior
    DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant that provides clear and concise answers."
    
    def __init__(self):
        """Initialize a Chatbot instance.
        
        The chatbot will create its own OpenAI client instance using environment variables
        and use a default system prompt to set the context for all conversations.
        """
        self._client = OpenAIClient(system_prompt=self.DEFAULT_SYSTEM_PROMPT)
    
    @property
    def client(self) -> OpenAIClient:
        """Get the OpenAI client instance.
        
        Returns:
            OpenAIClient: The OpenAI client instance being used by this chatbot.
        """
        return self._client
    
    def send_message(self, message: str) -> str:
        """Send a message to the chatbot and get the response.
        
        Args:
            message (str): The message to send.
            
        Returns:
            str: The chatbot's response message.
        """
        return self._client.send_message(message)
