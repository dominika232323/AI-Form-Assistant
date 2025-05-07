import json
import streamlit as st
from email_validator import validate_email, EmailNotValidError
from file_utils import read_json


def display_form(form_data=None):
    if form_data is None:
        form_data = {}

    form_data = load_form_data()

    if 'form_saved' not in st.session_state:
        st.session_state.form_saved = False

    with st.form("contact_form"):
        firstname = st.text_input("Firstname",
                                  value=form_data.get("firstname", ""),
                                  max_chars=20,
                                  key="firstname",
                                  disabled=True)

        lastname = st.text_input("Lastname",
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

        reason_of_contact = st.text_area("Reason of contact",
                                         value=form_data.get("reason", ""),
                                         max_chars=100,
                                         key="reason",
                                         disabled=True)

        urgency = st.slider("Urgency",
                            min_value=1,
                            max_value=10,
                            value=form_data.get("urgency", 5),
                            key="urgency",
                            disabled=True)

        submitted = st.form_submit_button("Save form")

        if submitted:
            st.session_state.saved_data = {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "reason": reason_of_contact,
                "urgency": urgency
            }
            st.session_state.form_saved = True
            st.success("Form saved successfully!")

    download_form()


def download_form():
    if st.session_state.get('form_saved'):
        json_data = json.dumps(st.session_state.saved_data, indent=4)

        st.download_button(
            label="Download form data as JSON",
            data=json_data,
            file_name="contact_form.json",
            mime="application/json"
        )


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
