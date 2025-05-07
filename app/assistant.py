import os
from google import genai
from dotenv import load_dotenv


def get_gemini_api_key():
    load_dotenv()
    return os.getenv("GEMINI_API_KEY")


def get_response(prompt: str, api_key: str=None, model: str="gemini-2.0-flash"):
    if api_key is None:
        api_key = get_gemini_api_key()

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model, contents=prompt
    )

    return response.text
