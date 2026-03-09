import streamlit as st
from funcvalidmark import get_valid_marks
from funcvalidname import get_valid_names
from funcvalidnum import get_valid_num_students
from funcyn import get_yes_no

def sem_marks():

    n = get_valid_num_students()

    st.header("Enter Marks for All Semesters")

    subjects = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]

    # ---------- SEMESTER 1 ----------
    st.subheader("Semester 1")

    i = {}

    for x in range(n):

        st.write(f"Student {x+1}")

        name = get_valid_names("Enter student name")

        marks = [
            get_valid_marks("Physics"),
            get_valid_marks("Chemistry"),
            get_valid_marks("Maths"),
            get_valid_marks("Computer"),
            get_valid_marks("Biology")
        ]

        if name:
            i[name] = marks

    last_target = None

    ch = get_yes_no("Do you want to find average for 1st sem?")

    if ch == "y":

        search = st.text_input("Whose average marks do you want to find?")

        if search in i:

            avg = sum(i[search]) / 5
            st.success(f"Average marks for 1st sem of {search} is {avg}")

            last_target = search

        elif search:
            st.error(f"Sorry, {search} not found.")

    # ---------- SEMESTER 2 ----------
    st.subheader("Semester 2")

    i1 = {}

    for name in i.keys():

        st.write(f"Entering marks for {name}")

        marks = [
            get_valid_marks("Physics"),
            get_valid_marks("Chemistry"),
            get_valid_marks("Maths"),
            get_valid_marks("Computer"),
            get_valid_marks("Biology")
        ]

        i1[name] = marks

    ch2 = get_yes_no("Do you want to find average for 2nd sem?")

    if ch2 == "y":

        if last_target:

            reuse = get_yes_no(f"Find average for same student ({last_target})?")

            current_target = last_target if reuse == "y" else st.text_input("Enter new student name")

        else:

            current_target = st.text_input("Enter student name")

        if current_target in i1:

            avg = sum(i1[current_target]) / 5
            st.success(f"Average for 2nd sem of {current_target} is {avg}")

            last_target = current_target

        elif current_target:
            st.error("Record not found.")

    # ---------- SEMESTER 3 ----------
    st.subheader("Semester 3")

    i2 = {}

    for name in i.keys():

        st.write(f"Entering marks for {name}")

        i2[name] = [
            get_valid_marks("Physics"),
            get_valid_marks("Chemistry"),
            get_valid_marks("Maths"),
            get_valid_marks("Computer"),
            get_valid_marks("Biology")
        ]

    ch3 = get_yes_no("Do you want to find average for 3rd sem?")

    if ch3 == "y":

        if last_target:

            reuse = get_yes_no(f"Find average for same student ({last_target})?")

            current_target = last_target if reuse == "y" else st.text_input("Enter new student name")

        else:

            current_target = st.text_input("Enter student name")

        if current_target in i2:

            avg = sum(i2[current_target]) / 5
            st.success(f"Average for 3rd sem of {current_target} is {avg}")

            last_target = current_target

        elif current_target:
            st.error("Record not found.")

    # ---------- SEMESTER 4 ----------
    st.subheader("Semester 4")

    i3 = {}

    for name in i.keys():

        st.write(f"Entering marks for {name}")

        i3[name] = [
            get_valid_marks("Physics"),
            get_valid_marks("Chemistry"),
            get_valid_marks("Maths"),
            get_valid_marks("Computer"),
            get_valid_marks("Biology")
        ]

    ch4 = get_yes_no("Do you want to find average for 4th sem?")

    if ch4 == "y":

        if last_target:

            reuse = get_yes_no(f"Find average for same student ({last_target})?")

            current_target = last_target if reuse == "y" else st.text_input("Enter new student name")

        else:

            current_target = st.text_input("Enter student name")

        if current_target in i3:

            avg = sum(i3[current_target]) / 5
            st.success(f"Average for 4th sem of {current_target} is {avg}")

            last_target = current_target

        elif current_target:
            st.error("Record not found.")

    return i, i1, i2, i3