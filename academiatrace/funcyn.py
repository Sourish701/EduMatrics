import streamlit as st

def get_yes_no(prompt_text):
    choice = st.radio(
        prompt_text,
        options=["Yes", "No"]
    )

    if choice == "Yes":
        return "y"
    else:
        return "n"