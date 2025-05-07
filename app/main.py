from assistant import get_response, get_gemini_api_key


if __name__ == "__main__":
    api_key = get_gemini_api_key()
    prompt = "Explain how AI works in a few words"
    response = get_response(prompt, api_key)
    print(response)
