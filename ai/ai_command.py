import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_command(user_command):
    # Check if the OpenAI API key is set
    if not openai.api_key:
        raise ValueError("OpenAI API key is not set")

    # Use OpenAI GPT-3.5-turbo model to generate content
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """You will generate a command a terminal understands based on the user command given, you will translate their command essentially. For example, "create a folder named rodeo"
                and you will return a command "mkdir rodeo". Do not return any other thing apart from the command. """,
            },
            {"role": "user", "content": f"The user command is {user_command}"},
        ],
    )

    # Extract the generated content from the API response
    generated_content = response["choices"][0]["message"]["content"]

    return generated_content
