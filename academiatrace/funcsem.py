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
        st.session_state.num_students_saved = 1

    # STEP 0: Get number of students
    if st.session_state.step == 0:
        with st.form("get_num_form"):
            st.subheader("Step 1: Enter Number of Students")
            n = st.number_input("Enter number of students:", min_value=1, max_value=50, value=1)
            submit = st.form_submit_button("Continue to Semester 1")
        
        if submit:
            st.session_state.num_students_saved = n
            st.session_state.step = 1
            st.rerun()
        return {}, {}, {}, {}

    n = st.session_state.num_students_saved

    # SEMESTER 1
    if st.session_state.step == 1:
        st.subheader("Semester 1 - Enter Student Details")

        with st.form("sem1_form"):
            student_data = {}
            
            for x in range(n):
                st.write(f"### Student {x+1}")

                name = get_valid_names(f"Enter student name", key=f"s1_name_{x}")

                marks = [
                    get_valid_marks("Physics", key=f"s1_phy_{x}"),
                    get_valid_marks("Chemistry", key=f"s1_chem_{x}"),
                    get_valid_marks("Maths", key=f"s1_math_{x}"),
                    get_valid_marks("Computer", key=f"s1_comp_{x}"),
                    get_valid_marks("Biology", key=f"s1_bio_{x}")
                ]

                if name:
                    student_data[x] = {"name": name, "marks": marks}

                st.divider()

            submit = st.form_submit_button("✅ Submit Semester 1")

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
                
                # Validate marks
                if not all(m is not None for m in marks):
                    errors.append(f"❌ Student {idx+1} ({name}): Please enter all marks!")
                    continue
                
                i[name] = marks
            
            if errors:
                for error in errors:
                    st.error(error)
                st.warning("Please fix the errors above and resubmit.")
            elif i:
                st.session_state.sem1_data = i
                st.session_state.step = 2
                st.success(f"✅ Saved {len(i)} students!")
                st.rerun()
            else:
                st.error("Please enter at least one valid student!")
        
        return {}, {}, {}, {}

    # SEMESTER 2
    if st.session_state.step == 2:
        st.subheader("Semester 2 - Enter Student Details")

        i = st.session_state.sem1_data

        with st.form("sem2_form"):
            i1 = {}
            
            for idx, name in enumerate(i.keys()):
                st.write(f"### {name}")

                marks = [
                    get_valid_marks("Physics", key=f"s2_phy_{idx}"),
                    get_valid_marks("Chemistry", key=f"s2_chem_{idx}"),
                    get_valid_marks("Maths", key=f"s2_math_{idx}"),
                    get_valid_marks("Computer", key=f"s2_comp_{idx}"),
                    get_valid_marks("Biology", key=f"s2_bio_{idx}")
                ]

                if all(m is not None for m in marks):
                    i1[name] = marks

                st.divider()

            submit = st.form_submit_button("✅ Submit Semester 2")

        if submit:
            if len(i1) == len(i):
                st.session_state.sem2_data = i1
                st.session_state.step = 3
                st.success(f"✅ Saved semester 2!")
                st.rerun()
            else:
                st.error("❌ Please enter marks for ALL students!")
        
        return st.session_state.sem1_data, {}, {}, {}

    # SEMESTER 3
    if st.session_state.step == 3:
        st.subheader("Semester 3 - Enter Student Details")

        i = st.session_state.sem1_data

        with st.form("sem3_form"):
            i2 = {}
            
            for idx, name in enumerate(i.keys()):
                st.write(f"### {name}")

                marks = [
                    get_valid_marks("Physics", key=f"s3_phy_{idx}"),
                    get_valid_marks("Chemistry", key=f"s3_chem_{idx}"),
                    get_valid_marks("Maths", key=f"s3_math_{idx}"),
                    get_valid_marks("Computer", key=f"s3_comp_{idx}"),
                    get_valid_marks("Biology", key=f"s3_bio_{idx}")
                ]

                if all(m is not None for m in marks):
                    i2[name] = marks

                st.divider()

            submit = st.form_submit_button("✅ Submit Semester 3")

        if submit:
            if len(i2) == len(i):
                st.session_state.sem3_data = i2
                st.session_state.step = 4
                st.success(f"✅ Saved semester 3!")
                st.rerun()
            else:
                st.error("❌ Please enter marks for ALL students!")
        
        return st.session_state.sem1_data, st.session_state.sem2_data, {}, {}

    # SEMESTER 4
    if st.session_state.step == 4:
        st.subheader("Semester 4 - Enter Student Details")

        i = st.session_state.sem1_data

        with st.form("sem4_form"):
            i3 = {}
            
            for idx, name in enumerate(i.keys()):
                st.write(f"### {name}")

                marks = [
                    get_valid_marks("Physics", key=f"s4_phy_{idx}"),
                    get_valid_marks("Chemistry", key=f"s4_chem_{idx}"),
                    get_valid_marks("Maths", key=f"s4_math_{idx}"),
                    get_valid_marks("Computer", key=f"s4_comp_{idx}"),
                    get_valid_marks("Biology", key=f"s4_bio_{idx}")
                ]

                if all(m is not None for m in marks):
                    i3[name] = marks

                st.divider()

            col1, col2 = st.columns(2)
            with col1:
                submit = st.form_submit_button("✅ Submit Semester 4")
            with col2:
                view_avg = st.form_submit_button("📊 View Averages")

        if submit:
            if len(i3) == len(i):
                st.session_state.sem4_data = i3
                st.session_state.step = 5
                st.success(f"✅ Saved semester 4!")
                st.rerun()
            else:
                st.error("❌ Please enter marks for ALL students!")

        if view_avg:
            if len(i3) == len(i):
                st.session_state.sem4_data = i3
                st.session_state.step = 5
                st.rerun()
            else:
                st.error("❌ Please enter marks for ALL students first!")

        return st.session_state.sem1_data, st.session_state.sem2_data, st.session_state.sem3_data, {}

    # STEP 5: View Averages
    if st.session_state.step == 5:
        st.subheader("📊 View Student Averages")

        i = st.session_state.sem1_data
        i1 = st.session_state.sem2_data
        i2 = st.session_state.sem3_data
        i3 = st.session_state.sem4_data

        with st.form("avg_form"):
            student = st.selectbox("Select student:", list(i.keys()))
            
            ch = get_yes_no("View averages?")
            submit = st.form_submit_button("Show Averages")

        if submit and ch == "y":
            st.write(f"### Averages for {student}")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                avg1 = sum(i[student]) / 5
                st.metric("Semester 1", f"{avg1:.2f}")
            
            with col2:
                avg2 = sum(i1[student]) / 5
                st.metric("Semester 2", f"{avg2:.2f}")
            
            with col3:
                avg3 = sum(i2[student]) / 5
                st.metric("Semester 3", f"{avg3:.2f}")
            
            with col4:
                avg4 = sum(i3[student]) / 5
                st.metric("Semester 4", f"{avg4:.2f}")

        if st.button("🔄 Go Back"):
            st.session_state.step = 0
            st.rerun()

        if st.button("🎉 Finish"):
            st.balloons()
            st.info("Thank you!")

        return i, i1, i2, i3


if __name__ == "__main__":
    sem_marks()