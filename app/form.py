import json
import streamlit as st
from email_validator import validate_email, EmailNotValidError
from file_utils import read_json


def display_form():
    form_data, newly_loaded = load_form_data()

    for key in ["firstname", "lastname", "email", "reason", "urgency"]:
        if key not in st.session_state:
            st.session_state[key] = form_data.get(key, "")

    if newly_loaded:
        st.session_state.firstname = form_data.get("firstname", "")
        st.session_state.lastname = form_data.get("lastname", "")
        st.session_state.email = form_data.get("email", "")
        st.session_state.reason = form_data.get("reason", "")
        st.session_state.urgency = form_data.get("urgency", "")

    st.subheader("Current Form Data")

    form_display = {
        "Firstname": st.session_state.firstname,
        "Lastname": st.session_state.lastname,
        "Email": st.session_state.email,
        "Reason of contact": st.session_state.reason,
        "Urgency": st.session_state.urgency
    }

    st.json(form_display)

    st.session_state.saved_data = {
        "firstname": st.session_state.firstname,
        "lastname": st.session_state.lastname,
        "email": st.session_state.email,
        "reason": st.session_state.reason,
        "urgency": st.session_state.urgency
    }

    download_form()


def download_form():
    if "saved_data" in st.session_state:
        json_data = json.dumps(st.session_state.saved_data, indent=4)

        st.download_button(
            label="Download form data as JSON",
            data=json_data,
            file_name="contact_form.json",
            mime="application/json"
        )


def load_form_data() -> tuple[dict, bool]:
    uploaded_file = st.file_uploader("Load your form from a JSON file", type=['json'])

    if uploaded_file is not None:
        try:
            if "last_uploaded_filename" not in st.session_state or uploaded_file.name != st.session_state.last_uploaded_filename:
                form_data = read_json(uploaded_file)
                st.session_state.loaded_form_data = form_data
                st.session_state.last_uploaded_filename = uploaded_file.name
                st.success("File loaded successfully!")

                return form_data, True  # <-- True means new file loaded

            return st.session_state.loaded_form_data, False

        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
            return {}, False

    return st.session_state.get("loaded_form_data", {}), False



def check_email(email: str) -> bool:
    try:
        validate_email(email)
        return True

    except EmailNotValidError:
        return False
