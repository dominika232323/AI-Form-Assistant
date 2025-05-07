from form import display_form
from chat import display_chat
import streamlit as st


def main():
    st.set_page_config(layout="wide")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Helpdesk Form")
        display_form()

    with col2:
        st.header("AI Assistant Chat")
        display_chat()


if __name__ == "__main__":
    main()
