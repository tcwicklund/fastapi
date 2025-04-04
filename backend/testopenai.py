from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if api_key is None:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable."
    )

# Initialize the OpenAI client
client = OpenAI()

client.api_key = api_key
response = client.responses.create(
    model="gpt-4o", input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
