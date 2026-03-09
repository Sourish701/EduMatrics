import streamlit as st

def get_valid_marks(prompt_text, key=None):
    """
    Get valid marks (0-100)
    Only works inside forms
    MUST pass a unique key parameter!
    """
    marks = st.number_input(
        prompt_text,
        min_value=0,
        max_value=100,
        step=1,
        key=key
    )

    if marks is not None:
        return int(marks)

    return None
