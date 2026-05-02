import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)


def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that always answers confidently."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

while True:
    q = input("Ask: ")
    print(ask_ai(q))