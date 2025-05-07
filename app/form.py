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
