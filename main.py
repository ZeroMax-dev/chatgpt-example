from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with local model endpoint
client = OpenAI(
    # base_url="http://127.0.0.1:1234/v1",
    api_key=os.getenv("OPENAI_API_KEY")  # May not be needed for local models but kept for compatibility
)

# doc is here https://platform.openai.com/docs/guides/chat/chat-vs-completions?utm_medium=email&_hsmi=248334739&utm_content=248334739&utm_source=hs_email
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        # system message first, it helps set the behavior of the assistant
        {"role": "system", "content": "You are a helpful assistant."},
        # I am the user, and this is my prompt
        {"role": "user", "content": "What's the best star wars movie?"},
        # we can also add the previous conversation
        # {"role": "assistant", "content": "Episode III."},
    ],
)
# let's see the reply
print(chat_completion.choices[0].message.content)
# As an AI language model, I cannot provide my personal opinion. However, according to critics and public reception, "The Empire Strikes Back" is often considered the best Star Wars movie.
