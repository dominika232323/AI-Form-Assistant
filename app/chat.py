import re
import streamlit as st

from form import update_form
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

        updated_data = extract_json(response.text)
        update_form(updated_data)


def extract_json(text):
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise ValueError("No JSON found in text.")
