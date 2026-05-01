import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

# --- rule-based examples ---
examples = [
    {"input": "Hi", "output": "Hello!"},
    {"input": "Bye", "output": "Goodbye!"}
]

# --- AI fallback ---
def chat(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


# --- main bot logic ---
def custom_bot(user_input):
    for ex in examples:
        if user_input == ex["input"]:
            return ex["output"]
    return chat(user_input)


# --- run interaction ---
user_input = input("You: ")
print("Bot:", custom_bot(user_input))