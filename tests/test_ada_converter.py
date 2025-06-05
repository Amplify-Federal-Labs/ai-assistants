import unittest
from unittest.mock import patch, MagicMock
from src.ada_converter import AdaConverter


class TestAdaConverter(unittest.TestCase):
    """Test cases for AdaConverter class."""
    
    @patch('src.ada_converter.OpenAIClient')
    def test_ada_converter_initializes_with_correct_system_prompt(self, mock_openai_client):
        """Test that AdaConverter initializes OpenAIClient with the correct system prompt."""
        # Arrange
        expected_system_prompt = (
            "You are a helpful code convertion agent. You will convert code written in Ada "
            "programming language into python. You will try to replicate the logic flow as "
            "much as possible. You will also write unit tests to verify those logic flows."
        )
        
        # Act
        ada_converter = AdaConverter()
        
        # Assert
        mock_openai_client.assert_called_once_with(system_prompt=expected_system_prompt)

    @patch('src.ada_converter.OpenAIClient')
    def test_convert_method_sends_correct_prompt_to_openai_client(self, mock_openai_client):
        """Test that convert method sends the correct prompt format to OpenAI client."""
        # Arrange
        mock_client_instance = MagicMock()
        mock_openai_client.return_value = mock_client_instance
        mock_client_instance.send_message.return_value = "converted python code"
        
        ada_code = "procedure Hello is\nbegin\n   Put_Line(\"Hello World\");\nend Hello;"
        expected_prompt = "Convert the following Ada code into Python\n" + ada_code
        
        ada_converter = AdaConverter()
        
        # Act
        result = ada_converter.convert(ada_code)
        
        # Assert
        mock_client_instance.send_message.assert_called_once_with(expected_prompt)
        self.assertEqual(result, "converted python code")


if __name__ == '__main__':
    unittest.main()