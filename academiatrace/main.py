import streamlit as st

# Import modules
import funcsem
import funchighpsem
import funchighpsub
import funcanalysis
import funchighsub4sem

st.title("EduMetrics Control Center")

st.markdown("---")

# STEP 1: DATA ENTRY
st.header("Data Entry Module")

if "data" not in st.session_state:
    st.session_state.data = None

if "data_entry_started" not in st.session_state:
    st.session_state.data_entry_started = False

# Get data from sem_marks (this runs the form steps)
i, i1, i2, i3 = funcsem.sem_marks()

# Only process analysis if ALL 4 semesters have data
if i and i1 and i2 and i3:
    # Store complete data in session state
    st.session_state.data = (i, i1, i2, i3)
    st.session_state.data_entry_started = True
    
    # Now show all the analysis sections
    
    # STEP 2: SEMESTER TOPPERS
    st.header("Toppers in Each Semester")
    
    funchighpsem.highest_in_1stsem(i)
    funchighpsem.highest_in_2ndsem(i1)
    funchighpsem.highest_in_3rdsem(i2)
    funchighpsem.highest_in_4thsem(i3)

    # STEP 3: OVERALL SUBJECT TOPPERS
    st.header("Overall Subject Toppers (Sem 1-4)")
    funchighsub4sem.show_overall_subject_toppers(i, i1, i2, i3)

    # STEP 4: SUBJECT TOPPERS
    st.header("Toppers in Each Subject")
    funchighpsub.find_highest_per_subject(i, i1, i2, i3)

    # STEP 5: STUDENT ANALYSIS
    st.header("Full Student Performance Analysis")
    funcanalysis.analysis(i, i1, i2, i3)

elif st.session_state.data_entry_started:
    st.info("Please complete all 4 semesters to view analysis...")
else:
    st.info("Start entering student marks above to begin!")