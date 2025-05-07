from assistant import get_response, get_gemini_api_key
import streamlit as st


def display_form(form_data: dict):
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

        st.text_input("Email",
                      value=form_data.get("email", ""),
                      key="email",
                      disabled=True)

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


def main():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Helpdesk Form")

        form_data = {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "reason": "I need help with a technical issue",
            "urgency": 5
        }
        display_form(form_data)

    with col2:
        st.header("AI Assistant Chat")

        api_key = get_gemini_api_key()
        prompt = "Explain how AI works in a few words"
        response = get_response(prompt, api_key)

        st.write(response)


if __name__ == "__main__":
    main()
