import re
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

        update_form(response)


def update_form(response):
    try:
        updated_data = extract_json(response.text)

        field_mapping = {
            "Firstname": "firstname",
            "Lastname": "lastname",
            "Email": "email",
            "Reason of contact": "reason",
            "Urgency": "urgency"
        }

        for gemini_key, state_key in field_mapping.items():
            value = updated_data.get(gemini_key, "")
            if value:
                st.session_state[state_key] = value

        st.success("Form updated based on Gemini's response!")
        st.rerun()

    except (json.JSONDecodeError, ValueError):
        st.warning(
            "Could not parse Gemini's response as JSON. Please make sure the assistant replies with valid JSON.")


def extract_json(text):
    # Find the first {...} block
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise ValueError("No JSON found in text.")
