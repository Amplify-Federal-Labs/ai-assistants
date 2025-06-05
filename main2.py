import os
import click
from dotenv import load_dotenv
from src.ada_converter import AdaConverter

def print_welcome():
    click.clear()
    click.secho("🔄 Ada to Python Converter", fg="blue", bold=True)
    click.secho("Type 'quit' to exit.", fg="yellow")
    click.secho("For multi-line input, type 'END' on a new line to finish.", fg="cyan")
    click.echo("-" * 50)

def print_user_message(message: str):
    click.echo()
    click.secho("Ada Code: ", fg="green", bold=True, nl=False)
    click.echo(message)

def print_converted_code(message: str):
    click.echo()
    click.secho("Python Code: ", fg="blue", bold=True, nl=False)
    click.echo(message)

def print_error(error: str):
    click.echo()
    click.secho("Error: ", fg="red", bold=True, nl=False)
    click.echo(error)

@click.command()
def main():
    """Convert Ada code to Python using OpenAI."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Create an AdaConverter instance
    ada_converter = AdaConverter()
    
    print_welcome()
    
    while True:
        # Get user input (multi-line)
        click.echo()
        click.secho("Enter Ada code (type 'END' on a new line to finish):", fg="green")
        
        lines = []
        while True:
            try:
                line = input()
                if line.strip().upper() == 'END':
                    break
                if line.strip().lower() == 'quit':
                    click.echo()
                    click.secho("👋 Goodbye!", fg="yellow")
                    return
                lines.append(line)
            except (EOFError, KeyboardInterrupt):
                click.echo()
                click.secho("👋 Goodbye!", fg="yellow")
                return
        
        ada_code = '\n'.join(lines).strip()
        
        if not ada_code:
            continue
            
        try:
            # Convert Ada code to Python
            python_code = ada_converter.convert(ada_code)
            print_converted_code(python_code)
            
        except Exception as e:
            print_error(str(e))

if __name__ == "__main__":
    main()