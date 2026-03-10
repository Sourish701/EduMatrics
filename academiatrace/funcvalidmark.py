import streamlit as st

def get_valid_marks(prompt_text, key=None):
    """
    Get valid marks (0-100)
    Accepts direct keyboard input
    Returns None if invalid, so form validation can handle it
    """
    marks_input = st.text_input(
        prompt_text,
        value="",
        key=key,
        placeholder="0-100"
    )
    
    if marks_input == "":
        return None
    
    try:
        marks = int(marks_input)
        if 0 <= marks <= 100:
            return marks
        else:
            return None  # Will be caught by form validation
    except ValueError:
        return None  # Will be caught by form validation