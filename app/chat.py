import streamlit as st
from assistant import get_response
import json


def display_chat():
    initialize_chat_history()
    display_chat_history()

    if prompt := st.chat_input("What would you like to ask Gemini?"):
        handle_user_prompt(prompt)


def initialize_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_prompt(prompt: str):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Gemini is thinking..."):
        response = get_response(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.text)

        st.session_state.messages.append({"role": "assistant", "content": response.text})

        clean_json_text = extract_json_from_response(response.text)
        update_form(clean_json_text)


def extract_json_from_response(text):
    if "```" in text:
        parts = text.split("```")

        for part in parts:
            if part.strip().startswith("{"):
                return part.strip()

            if part.strip().startswith("json"):
                return "\n".join(part.strip().split("\n")[1:]).strip()

    return text.strip()


def update_form(clean_json_text):
    try:
        response_data = json.loads(clean_json_text)

        for field, value in response_data.items():
            if field.lower() in ["firstname", "lastname", "email", "reason of contact", "urgency"]:
                key = field.lower().replace(" ", "")

                if key in st.session_state:
                    st.session_state[key] = value

    except json.JSONDecodeError as e:
        st.warning(f"Gemini's response wasn't valid JSON; no form fields were updated.\n\nError: {str(e)}")
