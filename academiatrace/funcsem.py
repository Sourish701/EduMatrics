import streamlit as st
from funcvalidmark import get_valid_marks
from funcvalidname import get_valid_names
from funcvalidnum import get_valid_num_students
from funcyn import get_yes_no

def sem_marks():
    
    st.header("Enter Marks for All Semesters")
    
    # Initialize session state for step navigation
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "num_students_saved" not in st.session_state:
        st.session_state.num_students_saved = 0
    if "data_entry_started" not in st.session_state:
        st.session_state.data_entry_started = False

    # STEP 0: Ask if user wants to start
    if st.session_state.step == 0 and not st.session_state.data_entry_started:
        st.subheader("🎓 Student Marks Entry System")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("✅ Start Data Entry", use_container_width=True, key="start_btn"):
                st.session_state.data_entry_started = True
                st.rerun()
        
        with col2:
            if st.button("❌ Exit", use_container_width=True, key="exit_btn"):
                st.info("Thank you for using the system!")
                return {}, {}, {}, {}
        
        st.info("👈 Click 'Start Data Entry' to begin entering student marks")
        return {}, {}, {}, {}

    # STEP 1: Get number of students
    if st.session_state.step == 0 and st.session_state.data_entry_started:
        with st.form("get_num_form"):
            st.subheader("Step 1: Enter Number of Students")
            st.write("How many students do you want to enter?")
            
            n = st.number_input(
                "Number of students:",
                min_value=1,
                max_value=100,
                value=1
            )
            
            submit = st.form_submit_button("Continue to Semester 1", use_container_width=True)
        
        if submit:
            st.session_state.num_students_saved = int(n)
            st.session_state.step = 1
            st.rerun()
        
        return {}, {}, {}, {}

    n = st.session_state.num_students_saved

    # SEMESTER 1
    if st.session_state.step == 1:
        st.subheader(f"Semester 1 - Enter Marks for {n} Students")
        st.info(f"📚 You are entering marks for {n} student(s). Please enter valid marks (0-100) for all students.")

        with st.form("sem1_form", clear_on_submit=False):
            student_data = {}
            
            for x in range(n):
                st.write(f"### Student {x+1}")

                name = get_valid_names(f"Enter student name", key=f"s1_name_{x}")

                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    physics = get_valid_marks("Physics", key=f"s1_phy_{x}")
                with col2:
                    chemistry = get_valid_marks("Chemistry", key=f"s1_chem_{x}")
                with col3:
                    maths = get_valid_marks("Maths", key=f"s1_math_{x}")
                with col4:
                    computer = get_valid_marks("Computer", key=f"s1_comp_{x}")
                with col5:
                    biology = get_valid_marks("Biology", key=f"s1_bio_{x}")

                marks = [physics, chemistry, maths, computer, biology]

                if name:
                    student_data[x] = {"name": name, "marks": marks}

                st.divider()

            submit = st.form_submit_button("✅ Submit Semester 1", use_container_width=True)

        if submit:
            i = {}
            errors = []
            
            for idx, data in student_data.items():
                name = data["name"]
                marks = data["marks"]
                
                # Validate name (alphabets only)
                if not name.replace(" ", "").isalpha():
                    errors.append(f"❌ Student {idx+1}: Invalid name '{name}'. Use alphabets only!")
                    continue
                
                # Validate marks - must be valid numbers between 0-100
                invalid_marks = []
                for i_idx, mark in enumerate(marks):
                    if mark is None or mark < 0 or mark > 100:
                        subjects = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]
                        invalid_marks.append(subjects[i_idx])
                
                if invalid_marks:
                    errors.append(f"❌ Student {idx+1} ({name}): Invalid marks in {', '.join(invalid_marks)}. Please enter marks between 0-100!")
                    continue
                
                i[name] = marks
            
            if errors:
                st.error("⚠️ Please fix the following errors:")
                for error in errors:
                    st.error(error)
                st.stop()  # Don't proceed until errors are fixed
            elif len(i) == n:
                st.session_state.sem1_data = i
                st.session_state.step = 2
                st.success(f"✅ Saved {len(i)} students! Moving to Semester 2...")
                st.rerun()
            else:
                st.error(f"❌ Please enter marks for ALL {n} students! You entered {len(i)} students.")
                st.stop()
        
        return {}, {}, {}, {}

    # SEMESTER 2
    if st.session_state.step == 2:
        st.subheader("Semester 2 - Enter Marks for All Students")

        i = st.session_state.sem1_data

        with st.form("sem2_form", clear_on_submit=False):
            i1 = {}
            
            for idx, name in enumerate(i.keys()):
                st.write(f"### {name}")

                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    physics = get_valid_marks("Physics", key=f"s2_phy_{idx}")
                with col2:
                    chemistry = get_valid_marks("Chemistry", key=f"s2_chem_{idx}")
                with col3:
                    maths = get_valid_marks("Maths", key=f"s2_math_{idx}")
                with col4:
                    computer = get_valid_marks("Computer", key=f"s2_comp_{idx}")
                with col5:
                    biology = get_valid_marks("Biology", key=f"s2_bio_{idx}")

                marks = [physics, chemistry, maths, computer, biology]

                # Check if all marks are valid
                if all(m is not None and 0 <= m <= 100 for m in marks):
                    i1[name] = marks

                st.divider()

            submit = st.form_submit_button("✅ Submit Semester 2", use_container_width=True)

        if submit:
            if len(i1) == len(i):
                st.session_state.sem2_data = i1
                st.session_state.step = 3
                st.success(f"✅ Saved Semester 2! Moving to Semester 3...")
                st.rerun()
            else:
                st.error(f"❌ Please enter VALID marks for ALL {len(i)} students! You completed {len(i1)} students.")
                st.stop()
        
        return st.session_state.sem1_data, {}, {}, {}

    # SEMESTER 3
    if st.session_state.step == 3:
        st.subheader("Semester 3 - Enter Marks for All Students")

        i = st.session_state.sem1_data

        with st.form("sem3_form", clear_on_submit=False):
            i2 = {}
            
            for idx, name in enumerate(i.keys()):
                st.write(f"### {name}")

                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    physics = get_valid_marks("Physics", key=f"s3_phy_{idx}")
                with col2:
                    chemistry = get_valid_marks("Chemistry", key=f"s3_chem_{idx}")
                with col3:
                    maths = get_valid_marks("Maths", key=f"s3_math_{idx}")
                with col4:
                    computer = get_valid_marks("Computer", key=f"s3_comp_{idx}")
                with col5:
                    biology = get_valid_marks("Biology", key=f"s3_bio_{idx}")

                marks = [physics, chemistry, maths, computer, biology]

                if all(m is not None and 0 <= m <= 100 for m in marks):
                    i2[name] = marks

                st.divider()

            submit = st.form_submit_button("✅ Submit Semester 3", use_container_width=True)

        if submit:
            if len(i2) == len(i):
                st.session_state.sem3_data = i2
                st.session_state.step = 4
                st.success(f"✅ Saved Semester 3! Moving to Semester 4...")
                st.rerun()
            else:
                st.error(f"❌ Please enter VALID marks for ALL {len(i)} students! You completed {len(i2)} students.")
                st.stop()
        
        return st.session_state.sem1_data, st.session_state.sem2_data, {}, {}

    # SEMESTER 4
    if st.session_state.step == 4:
        st.subheader("Semester 4 - Enter Marks for All Students")

        i = st.session_state.sem1_data

        with st.form("sem4_form", clear_on_submit=False):
            i3 = {}
            
            for idx, name in enumerate(i.keys()):
                st.write(f"### {name}")

                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    physics = get_valid_marks("Physics", key=f"s4_phy_{idx}")
                with col2:
                    chemistry = get_valid_marks("Chemistry", key=f"s4_chem_{idx}")
                with col3:
                    maths = get_valid_marks("Maths", key=f"s4_math_{idx}")
                with col4:
                    computer = get_valid_marks("Computer", key=f"s4_comp_{idx}")
                with col5:
                    biology = get_valid_marks("Biology", key=f"s4_bio_{idx}")

                marks = [physics, chemistry, maths, computer, biology]

                if all(m is not None and 0 <= m <= 100 for m in marks):
                    i3[name] = marks

                st.divider()

            col1, col2 = st.columns(2)
            with col1:
                submit = st.form_submit_button("✅ Submit & View Analysis", use_container_width=True)
            with col2:
                restart = st.form_submit_button("🔄 Start Over", use_container_width=True)

        if submit:
            if len(i3) == len(i):
                st.session_state.sem4_data = i3
                st.session_state.step = 5
                st.success(f"✅ All data saved! Showing analysis...")
                st.rerun()
            else:
                st.error(f"❌ Please enter VALID marks for ALL {len(i)} students! You completed {len(i3)} students.")
                st.stop()

        if restart:
            st.session_state.step = 0
            st.session_state.data_entry_started = False
            st.session_state.num_students_saved = 0
            st.rerun()

        return st.session_state.sem1_data, st.session_state.sem2_data, st.session_state.sem3_data, {}

    # STEP 5: All data complete - return for analysis
    if st.session_state.step == 5:
        i = st.session_state.sem1_data
        i1 = st.session_state.sem2_data
        i2 = st.session_state.sem3_data
        i3 = st.session_state.sem4_data

        return i, i1, i2, i3


if __name__ == "__main__":
    sem_marks()