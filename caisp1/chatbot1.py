import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env from current folder automatically
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def chat(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


while True:
    msg = input("You: ")
    print("Bot:", chat(msg))