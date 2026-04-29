import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
api_key = os.getenv("GROQ_API_KEY")


print("API KEY:", api_key)   
client = Groq(api_key=api_key)




try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "What is NDA?"}
        ],
        temperature=0.3,
        max_tokens=100
    )

    print("SUCCESS")
    print(response.choices[0].message.content)

except Exception as e:
    print("ERROR:", e)

    