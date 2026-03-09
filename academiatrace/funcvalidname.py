import streamlit as st

def get_valid_names(prompt_text, key=None):
    """
    Get valid student name and validate it
    Returns cleaned name or None
    Use ONLY inside st.form()
    """
    name = st.text_input(prompt_text, key=key)

    if name:
        clean_name = name.strip()

        # validation - just return None if invalid, don't show error (errors don't work well in forms)
        if clean_name.replace(" ", "").isalpha():
            return clean_name
        else:
            return None  # Invalid name

    return None