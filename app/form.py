import json
from typing import Any

import streamlit as st
from email_validator import validate_email, EmailNotValidError
from file_utils import read_json


def display_form() -> None:
    form_data, newly_loaded = load_form_data()

    for key in ["firstname", "lastname", "email", "reason_of_contact", "urgency"]:
        if key not in st.session_state:
            st.session_state[key] = form_data.get(key, "")

    if newly_loaded:
        st.session_state.firstname = form_data.get("firstname", "")
        st.session_state.lastname = form_data.get("lastname", "")
        st.session_state.email = form_data.get("email", "")
        st.session_state.reason_of_contact = form_data.get("reason_of_contact", "")
        st.session_state.urgency = form_data.get("urgency", "")

    st.subheader("Current Form Data")

    form_display = {
        "Firstname": st.session_state.firstname,
        "Lastname": st.session_state.lastname,
        "Email": st.session_state.email,
        "Reason of contact": st.session_state.reason_of_contact,
        "Urgency": st.session_state.urgency,
    }

    st.json(form_display)

    st.session_state.saved_data = {
        "firstname": st.session_state.firstname,
        "lastname": st.session_state.lastname,
        "email": st.session_state.email,
        "reason_of_contact": st.session_state.reason_of_contact,
        "urgency": st.session_state.urgency,
    }

    download_form()


def download_form() -> None:
    if "saved_data" in st.session_state:
        json_data = json.dumps(st.session_state.saved_data, indent=4)

        st.download_button(
            label="Download form data as JSON",
            data=json_data,
            file_name="contact_form.json",
            mime="application/json",
        )


def load_form_data() -> tuple[dict, bool]:
    uploaded_file = st.file_uploader("Load your form from a JSON file", type=["json"])

    if uploaded_file is not None:
        try:
            if (
                "last_uploaded_filename" not in st.session_state
                or uploaded_file.name != st.session_state.last_uploaded_filename
            ):
                form_data = read_json(uploaded_file)
                st.session_state.loaded_form_data = form_data
                st.session_state.last_uploaded_filename = uploaded_file.name
                st.success("File loaded successfully!")

                validate_loaded_data(form_data)

                return form_data, True

            return st.session_state.loaded_form_data, False

        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
            return {}, False

    return st.session_state.get("loaded_form_data", {}), False


def validate_loaded_data(form_data: dict) -> None:
    remove_wrong_data_from_loaded_data(form_data, "firstname", validate_firstname)
    remove_wrong_data_from_loaded_data(form_data, "lastname", validate_lastname)
    remove_wrong_data_from_loaded_data(form_data, "email", validate_email_value)
    remove_wrong_data_from_loaded_data(
        form_data, "reason_of_contact", validate_reason_of_contact
    )
    remove_wrong_data_from_loaded_data(form_data, "urgency", validate_urgency)


def remove_wrong_data_from_loaded_data(
    form_data: dict, field: str, validation_func
) -> None:
    error = validation_func(form_data.get(field, ""))

    if error:
        form_data[field] = ""
        st.error(error)


def check_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def update_form(updated_data: dict) -> None:
    try:
        field_mapping = {
            "Firstname": "firstname",
            "Lastname": "lastname",
            "Email": "email",
            "Reason of contact": "reason_of_contact",
            "Urgency": "urgency",
        }

        errors = []

        for gemini_key, state_key in field_mapping.items():
            value = updated_data.get(gemini_key, "")

            if gemini_key == "Firstname":
                error = validate_firstname(value)
            elif gemini_key == "Lastname":
                error = validate_lastname(value)
            elif gemini_key == "Email":
                error = validate_email_value(value)
            elif gemini_key == "Reason of contact":
                error = validate_reason_of_contact(value)
            elif gemini_key == "Urgency":
                error = validate_urgency(value)
            else:
                error = None

            if error:
                errors.append(error)
            else:
                if value != "":
                    st.session_state[state_key] = value

        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("Form updated based on Gemini's response!")
            st.rerun()

    except (json.JSONDecodeError, ValueError):
        st.warning(
            "Could not parse Gemini's response as JSON. Please make sure the assistant replies with valid JSON."
        )


def validate_firstname(value: Any) -> str | None:
    if not isinstance(value, str):
        return "Firstname must be a string."
    elif len(value) > 20:
        return "Firstname must be at most 20 characters."
    return None


def validate_lastname(value: Any) -> str | None:
    if not isinstance(value, str):
        return "Lastname must be a string."
    elif len(value) > 20:
        return "Lastname must be at most 20 characters."
    return None


def validate_email_value(value: Any) -> str | None:
    if not isinstance(value, str):
        return "Email must be a string."
    elif value and not check_email(value):
        return "Invalid email format."
    return None


def validate_reason_of_contact(value: Any) -> str | None:
    if not isinstance(value, str):
        return "Reason of contact must be a string."
    elif len(value) > 100:
        return "Reason of contact must be at most 100 characters."
    return None


def validate_urgency(value: Any) -> str | None:
    if value != "":
        try:
            urgency_int = int(value)
            if 1 <= urgency_int <= 10:
                return None
            else:
                return "Urgency must be an integer between 1 and 10."
        except ValueError:
            return "Urgency must be an integer between 1 and 10."
    return None
