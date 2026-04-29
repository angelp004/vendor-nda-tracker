


from services.groq_client import GroqClient

client = GroqClient()

try:
    result = client.generate_response("Explain NDA in simple words")

    print("SUCCESS")
    print(result)

except Exception as e:
    print("ERROR:", e)