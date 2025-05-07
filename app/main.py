from form import display_form
from assistant import get_response, get_gemini_api_key
import streamlit as st


def main():
    st.set_page_config(layout="wide")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Helpdesk Form")
        display_form()

    with col2:
        st.header("AI Assistant Chat")

        api_key = get_gemini_api_key()
        prompt = "Explain how AI works in a few words"
        response = get_response(prompt, api_key)

        st.write(response)


if __name__ == "__main__":
    main()
