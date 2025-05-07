import streamlit as st
from email_validator import validate_email, EmailNotValidError
from file_utils import read_json


def display_form(form_data=None):
    if form_data is None:
        form_data = {}

    form_data = load_form_data()

    with st.form("contact_form"):
        st.text_input("Firstname",
                      value=form_data.get("firstname", ""),
                      max_chars=20,
                      key="firstname",
                      disabled=True)

        st.text_input("Lastname",
                      value=form_data.get("lastname", ""),
                      max_chars=20,
                      key="lastname",
                      disabled=True)

        email = st.text_input("Email",
                              value=form_data.get("email", ""),
                              key="email",
                              disabled=True)

        if email and not check_email(email):
            st.warning("Please enter a valid email address")

        st.text_area("Reason of contact",
                     value=form_data.get("reason", ""),
                     max_chars=100,
                     key="reason",
                     disabled=True)

        st.slider("Urgency",
                  min_value=1,
                  max_value=10,
                  value=form_data.get("urgency", 5),
                  key="urgency",
                  disabled=True)


def load_form_data() -> dict:
    uploaded_file = st.file_uploader("Load your form from a JSON file", type=['json'])

    if uploaded_file is not None:
        try:
            st.success("File loaded successfully!")
            return read_json(uploaded_file)
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
            return {}

    return {}


def check_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
