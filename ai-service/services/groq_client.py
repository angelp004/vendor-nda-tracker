import os
import logging
from groq import Groq
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

# Load .env
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GroqClient:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        


        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found")

        self.client = Groq(api_key=self.api_key)

        # Use working model
        self.model = "llama-3.1-8b-instant"
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def  generate_response(self, text):
        try:
            prompt = f"""
You are a legal expert.

Explain the NDA clearly.

IMPORTANT:
- Highlight risks clearly
- Mention penalties
- Give a simple example

Text:
{text}
"""
           

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=300
            )

            output = response.choices[0].message.content

            logger.info("AI response generated successfully")

            return {
                "success": True,
                "response": output
            }

        except Exception as e:
            logger.error(f"Groq API error: {str(e)}")
            raise