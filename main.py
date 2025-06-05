import os
import click
from dotenv import load_dotenv
from src.chatbot import Chatbot

def print_welcome():
    click.clear()
    click.secho("🤖 AI Assistant", fg="blue", bold=True)
    click.secho("Type 'quit' to exit.", fg="yellow")
    click.echo("-" * 50)

def print_user_message(message: str):
    click.echo()
    click.secho("You: ", fg="green", bold=True, nl=False)
    click.echo(message)

def print_assistant_message(message: str):
    click.echo()
    click.secho("Assistant: ", fg="blue", bold=True, nl=False)
    click.echo(message)

def print_error(error: str):
    click.echo()
    click.secho("Error: ", fg="red", bold=True, nl=False)
    click.echo(error)

@click.command()
def main():
    """An interactive AI assistant powered by OpenAI."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Create a chatbot instance
    chatbot = Chatbot()
    
    print_welcome()
    
    while True:
        # Get user input
        user_message = click.prompt("\nYou", type=str, prompt_suffix=" > ").strip()
        
        if user_message.lower() == 'quit':
            click.echo()
            click.secho("👋 Goodbye!", fg="yellow")
            break
            
        if not user_message:
            continue
            
        try:
            # Get chatbot's response
            response = chatbot.send_message(user_message)
            print_assistant_message(response)
            
        except Exception as e:
            print_error(str(e))

if __name__ == "__main__":
    main()
