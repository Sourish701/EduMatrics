import streamlit as st

def get_valid_marks(prompt_text, key=None):
    """
    Get valid marks (0-100)
    Accepts direct keyboard input
    Validates input properly
    """
    marks_input = st.text_input(
        prompt_text,
        value="",
        key=key,
        placeholder="0-100"
    )
    
    if marks_input == "":
        return 0  # Default to 0 if empty (will be caught later)
    
    try:
        marks = int(marks_input)
        if 0 <= marks <= 100:
            return marks
        else:
            st.error(f"❌ Marks must be between 0-100, got {marks}")
            return None
    except ValueError:
        st.error(f"❌ Invalid input: '{marks_input}'. Please enter a valid number.")
        return None