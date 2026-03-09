import streamlit as st

def get_valid_marks(prompt_text):
    marks = st.number_input(
        prompt_text,
        min_value=0,
        max_value=100,
        step=1
    )

    if marks is not None:
        return int(marks)

    return None