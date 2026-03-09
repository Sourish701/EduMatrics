import streamlit as st

def show_overall_subject_toppers(i, i1, i2, i3):

    subjects = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]
    student_names = list(i.keys())

    st.markdown("## OVERALL SUBJECT TOPPERS (SEM 1-4)")

    results = []

    for index in range(len(subjects)):

        max_total_mark = -1
        toppers = []

        for name in student_names:

            total_subject_mark = (
                i[name][index]
                + i1[name][index]
                + i2[name][index]
                + i3[name][index]
            )

            if total_subject_mark > max_total_mark:
                max_total_mark = total_subject_mark
                toppers = [name]

            elif total_subject_mark == max_total_mark:
                toppers.append(name)

        topper_names = ", ".join(toppers)

        results.append({
            "Subject": subjects[index],
            "Topper(s)": topper_names,
            "Total Marks": f"{max_total_mark}/400"
        })

    st.table(results)