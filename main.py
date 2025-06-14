import os
from dotenv import load_dotenv
from google import genai

MODEL = "gemini-2.0-flash-001"

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=MODEL,
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
)

print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print(response.text)
