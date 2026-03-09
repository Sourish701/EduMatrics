import streamlit as st

def get_valid_names(prompt_text):
    name = st.text_input(prompt_text)

    if name:
        clean_name = name.strip()

        # validation
        if clean_name.replace(" ", "").isalpha():
            st.success("Valid name entered.")
            return clean_name
        else:
            st.error("Invalid name! Please enter only alphabets.")

    return None