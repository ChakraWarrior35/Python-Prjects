import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("key")
)


client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)

print(resp.choices[0].message.content)
