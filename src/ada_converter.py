from src.api import OpenAIClient


class AdaConverter:
    """A converter for transforming Ada programming language code to Python."""
    
    def __init__(self):
        """Initialize the AdaConverter with the appropriate system prompt."""
        system_prompt = (
            "You are a helpful code convertion agent. You will convert code written in Ada "
            "programming language into python. You will try to replicate the logic flow as "
            "much as possible. You will also write unit tests to verify those logic flows."
        )
        
        self.client = OpenAIClient(system_prompt=system_prompt)
    
    def convert(self, code: str) -> str:
        """Convert Ada code to Python.
        
        Args:
            code (str): The Ada code to convert.
            
        Returns:
            str: The converted Python code.
        """
        prompt = "Convert the following Ada code into Python\n" + code
        return self.client.send_message(prompt)