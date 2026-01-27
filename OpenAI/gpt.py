from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.getenv("API_KEY")
)

prompt = input("Enter your prompt: ")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", 
          "content": prompt},
    ],
    model="gpt-5-nano",
)

print(chat_completion.choices[0].message.content)