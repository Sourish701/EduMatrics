import streamlit as st

def get_yes_no(prompt_text):
    """
    Get yes/no answer using selectbox (doesn't trigger rerun on change)
    Only works inside forms
    """
    choice = st.selectbox(
        prompt_text,
        options=["Yes", "No"],
        key=f"yn_{id(prompt_text)}"  # Unique key based on prompt
    )

    if choice == "Yes":
        return "y"
    else:
        return "n"