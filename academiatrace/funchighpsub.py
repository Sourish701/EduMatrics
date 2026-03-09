import streamlit as st

def find_highest_per_subject(i, i1, i2, i3):

    st.markdown("## SUBJECT-WISE HIGHEST MARKS SEARCH")

    # 1️⃣ Semester selection
    chosen_sem = st.selectbox(
        "Select Semester",
        ["1", "2", "3", "4"]
    )

    if chosen_sem == "1":
        marks_data = i
    elif chosen_sem == "2":
        marks_data = i1
    elif chosen_sem == "3":
        marks_data = i2
    else:
        marks_data = i3

    # 2️⃣ Subject selection
    subjects = ["physics", "chemistry", "maths", "computer", "biology"]

    chosen_sub = st.selectbox(
        "Select Subject",
        subjects
    )

    sub_index = subjects.index(chosen_sub)

    # 3️⃣ Calculation Logic (same as original)
    max_subject_mark = -1
    top_stud_names = []

    for name, marks_list in marks_data.items():

        current_marks = marks_list[sub_index]

        if current_marks > max_subject_mark:
            max_subject_mark = current_marks
            top_stud_names = [name]

        elif current_marks == max_subject_mark:
            top_stud_names.append(name)

    # 4️⃣ Display Result
    if marks_data:

        st.markdown("### RESULT")

        st.write(f"Semester: {chosen_sem}")
        st.write(f"Subject: {chosen_sub.capitalize()}")
        st.write(f"Highest Marks: **{max_subject_mark}**")
        st.success(f"Received by: {', '.join(top_stud_names)}")

    else:
        st.warning("No data available for this semester.")