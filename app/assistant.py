import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def get_gemini_api_key():
    load_dotenv()
    return os.getenv("GEMINI_API_KEY")


def get_response(prompt: str, api_key: str=None, model: str="gemini-2.0-flash"):
    if api_key is None:
        api_key = get_gemini_api_key()

    client = genai.Client(api_key=api_key)

    system_prompt = (
        "You are an assistant helping the user fill out a contact form. "
        "The form has the following fields: Firstname, Lastname, Email, Reason of contact, and Urgency (1-10). "
        "Ask questions one at a time and gather these details. "
        "Reply ONLY with JSON containing the fields you've filled in, like: "
        '{"Firstname": "John", "Lastname": "", "Email": "", "Reason of contact": "", "Urgency": ""}. '
        "If you don't have an answer for a field yet, leave it empty."
    )

    response = client.models.generate_content(
        model=model,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
        contents=prompt
    )

    return response
