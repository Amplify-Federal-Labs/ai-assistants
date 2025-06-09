from app.services.openai_client import OpenAIClient


class AdaConverter:
    """A converter for transforming Ada programming language code to Python."""
    
    def __init__(self):
        """Initialize the AdaConverter with the appropriate system prompt."""
        system_prompt = (
            "You are a helpful code convertion agent. "
            "You will convert code written in Ada programming language into python. "
            "You will firt describe the logic within Ada code. "
            "You will then convert the code into Python, while maintaining overall structure as much as possible. "
            "You will then write unit tests by reverse-engineering the python code."
            "You will return the response in the following format: "
            "# Logc"
            "<logic wihtin the original Ada code>"
            "# Unit Tests"
            "<Unit Tests written in Python based on the extracted logc>"
            "# Python Code"
            "<Resulting Python Code>"
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