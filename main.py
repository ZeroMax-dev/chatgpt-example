import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API endpoint for chat completions
api_url = "https://api.openai.com/v1/chat/completions"

# Set headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Prepare the request payload
# doc is here https://platform.openai.com/docs/guides/chat/chat-vs-completions
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        # system message first, it helps set the behavior of the assistant
        {"role": "system", "content": "You are a helpful assistant."},
        # I am the user, and this is my prompt
        {"role": "user", "content": "What's the best star wars movie?"},
        # we can also add the previous conversation
        # {"role": "assistant", "content": "Episode III."},
    ]
}

# Make the API request
response = requests.post(api_url, headers=headers, json=payload)

# Parse the response
if response.status_code == 200:
    # Extract and print the response content
    response_data = response.json()
    message_content = response_data['choices'][0]['message']['content']
    print(message_content)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
