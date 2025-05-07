import os
from google import genai
from dotenv import load_dotenv


def get_gemini_api_key():
    load_dotenv()
    return os.getenv("GEMINI_API_KEY")


def get_response(prompt, api_key, model="gemini-2.0-flash"):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model, contents=prompt
    )

    return response.text
