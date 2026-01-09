import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

messages = []

client = OpenAI(
    api_key=os.getenv("key")
)

def completion(message):
    global messages
    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Chette: {reply}")

if __name__ == "__main__":
    print("Chette: Hi I am Chette, How may I help you\n")
    while True:
        user_question = input("User: ")
        completion(user_question)
