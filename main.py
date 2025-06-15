import os

import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-2.0-flash-001"

verbose_output = False


def verbose_print(*args, **kwargs):
    if verbose_output:
        print(args, kwargs)


if len(sys.argv) < 2:
    print("Usage: main.py <prompt to llm>")
    exit(1)

if len(sys.argv) == 3:
    if sys.argv[2] == "--verbose":
        verbose_output = True


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


user_prompt = sys.argv[1]

verbose_print("User prompt:", user_prompt)


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model=MODEL,
    contents=messages,
)

verbose_print("Prompt tokens:", response.usage_metadata.prompt_token_count)
verbose_print("Response tokens:", response.usage_metadata.candidates_token_count)
print(response.text)
