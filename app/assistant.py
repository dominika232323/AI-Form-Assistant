from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL


def get_response(prompt: str):
    client = genai.Client(api_key=GEMINI_API_KEY)

    system_prompt = (
        "You are an assistant helping the user fill out a contact form. "
        "The form has the following fields: Firstname, Lastname, Email, Reason of contact, and Urgency (1-10). "
        "Ask questions one at a time and gather these details. "
        "Reply ONLY with JSON containing the fields you've filled in, like: "
        '{"Firstname": "John", "Lastname": "", "Email": "", "Reason of contact": "", "Urgency": ""}. '
        "If you don't have an answer for a field yet, leave it empty."
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
        contents=prompt
    )

    return response
