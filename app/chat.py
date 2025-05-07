import streamlit as st
from assistant import get_response


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
