import streamlit as st

def get_valid_num_students():

    m = st.number_input(
        "Enter number of students:",
        min_value=1,
        step=1
    )

    if m:
        return int(m)

    return None