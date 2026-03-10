import streamlit as st
import pandas as pd
from datetime import datetime

def generate_report_card(i, i1, i2, i3):
    """
    Generate report cards for all students
    Shows semester-wise performance, averages, and overall ranking
    """
    
    st.header("📋 Student Report Cards")
    
    # Get all students
    all_students = list(i.keys())
    
    # Calculate overall performance
    cumulative_totals = {}
    for name in all_students:
        total = sum(i[name]) + sum(i1[name]) + sum(i2[name]) + sum(i3[name])
        cumulative_totals[name] = total
    
    # Sort students by total marks
    sorted_students = sorted(cumulative_totals.items(), key=lambda x: x[1], reverse=True)
    
    # Select student to view report card
    st.subheader("Select Student")
    selected_student = st.selectbox("Choose a student to view their report card:", all_students)
    
    if selected_student:
        st.divider()
        
        # Calculate student rank
        student_rank = next((idx + 1 for idx, (name, _) in enumerate(sorted_students) if name == selected_student), None)
        
        # Get marks for selected student
        sem1_marks = i[selected_student]
        sem2_marks = i1[selected_student]
        sem3_marks = i2[selected_student]
        sem4_marks = i3[selected_student]
        
        # Calculate averages
        avg1 = sum(sem1_marks) / 5
        avg2 = sum(sem2_marks) / 5
        avg3 = sum(sem3_marks) / 5
        avg4 = sum(sem4_marks) / 5
        
        # Calculate total
        total_marks = sum(sem1_marks) + sum(sem2_marks) + sum(sem3_marks) + sum(sem4_marks)
        overall_avg = total_marks / 20
        
        # Display Report Card
        st.markdown(f"""
        <div style="border: 3px solid #1f77b4; padding: 20px; border-radius: 10px; background-color: #f0f8ff;">
            <h2 style="text-align: center; color: #1f77b4;">📚 STUDENT REPORT CARD</h2>
            <hr>
            <h3 style="text-align: center; color: #333;">Name: <span style="color: #1f77b4;">{selected_student}</span></h3>
            <h4 style="text-align: center; color: #666;">Rank: <span style="color: #ff7f0e; font-size: 24px;">#{student_rank} out of {len(all_students)}</span></h4>
            <hr>
        </div>
        """, unsafe_allow_html=True)
        
        # Semester-wise performance
        st.subheader("📊 Semester-wise Performance")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Semester 1 Avg", f"{avg1:.2f}/100")
        with col2:
            st.metric("Semester 2 Avg", f"{avg2:.2f}/100")
        with col3:
            st.metric("Semester 3 Avg", f"{avg3:.2f}/100")
        with col4:
            st.metric("Semester 4 Avg", f"{avg4:.2f}/100")
        
        st.divider()
        
        # Subject-wise performance across all semesters
        st.subheader("📈 Subject-wise Total Marks (All Semesters)")
        
        subjects = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]
        subject_totals = {}
        
        for idx, subject in enumerate(subjects):
            total = sem1_marks[idx] + sem2_marks[idx] + sem3_marks[idx] + sem4_marks[idx]
            subject_totals[subject] = total
        
        # Create subject performance dataframe
        subject_df = pd.DataFrame({
            "Subject": list(subject_totals.keys()),
            "Total Marks": list(subject_totals.values()),
            "Average": [val / 4 for val in subject_totals.values()]
        })
        
        st.dataframe(subject_df, use_container_width=True)
        
        st.divider()
        
        # Detailed semester breakdown
        st.subheader("📝 Detailed Semester Breakdown")
        
        # Semester 1
        st.write("#### Semester 1")
        sem1_df = pd.DataFrame({
            "Subject": subjects,
            "Marks": sem1_marks
        })
        st.dataframe(sem1_df, use_container_width=True)
        st.write(f"**Average: {avg1:.2f}/100**")
        
        # Semester 2
        st.write("#### Semester 2")
        sem2_df = pd.DataFrame({
            "Subject": subjects,
            "Marks": sem2_marks
        })
        st.dataframe(sem2_df, use_container_width=True)
        st.write(f"**Average: {avg2:.2f}/100**")
        
        # Semester 3
        st.write("#### Semester 3")
        sem3_df = pd.DataFrame({
            "Subject": subjects,
            "Marks": sem3_marks
        })
        st.dataframe(sem3_df, use_container_width=True)
        st.write(f"**Average: {avg3:.2f}/100**")
        
        # Semester 4
        st.write("#### Semester 4")
        sem4_df = pd.DataFrame({
            "Subject": subjects,
            "Marks": sem4_marks
        })
        st.dataframe(sem4_df, use_container_width=True)
        st.write(f"**Average: {avg4:.2f}/100**")
        
        st.divider()
        
        # Overall performance
        st.subheader("🏆 Overall Performance")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Marks", f"{total_marks}/2000")
        with col2:
            st.metric("Overall Average", f"{overall_avg:.2f}/100")
        with col3:
            # Determine grade
            if overall_avg >= 90:
                grade = "A+"
                color = "🌟"
            elif overall_avg >= 80:
                grade = "A"
                color = "⭐"
            elif overall_avg >= 70:
                grade = "B"
                color = "👍"
            elif overall_avg >= 60:
                grade = "C"
                color = "✓"
            else:
                grade = "D"
                color = "⚠️"
            
            st.metric("Grade", f"{color} {grade}")
        
        st.divider()
        
        # Analysis
        st.subheader("📌 Performance Analysis")
        
        # Strongest subject
        strongest = max(subject_totals, key=subject_totals.get)
        strongest_total = subject_totals[strongest]
        
        # Weakest subject
        weakest = min(subject_totals, key=subject_totals.get)
        weakest_total = subject_totals[weakest]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success(f"✅ **Strongest Subject:** {strongest} ({strongest_total}/400)")
        
        with col2:
            st.warning(f"⚠️ **Subject to Improve:** {weakest} ({weakest_total}/400)")
        
        # Comparison with class average
        class_avg = sum(cumulative_totals.values()) / len(cumulative_totals)
        student_total = cumulative_totals[selected_student]
        diff = student_total - class_avg
        
        st.info(f"📊 **Class Average Total:** {class_avg:.2f}/400")
        
        if diff > 0:
            st.success(f"✅ **{selected_student}** is {diff:.2f} marks above the class average!")
        elif diff < 0:
            st.warning(f"⚠️ **{selected_student}** is {abs(diff):.2f} marks below the class average. Room for improvement!")
        else:
            st.info(f"**{selected_student}** is at the class average.")
        
        st.divider()
        
        # Class ranking table
        st.subheader("🏅 Class Rankings")
        
        ranking_data = []
        for rank, (name, total) in enumerate(sorted_students, 1):
            avg = total / 20
            ranking_data.append({
                "Rank": rank,
                "Student Name": name,
                "Total Marks": total,
                "Average": f"{avg:.2f}"
            })
        
        ranking_df = pd.DataFrame(ranking_data)
        st.dataframe(ranking_df, use_container_width=True)
        
        # Highlight current student
        current_student_rank = ranking_df[ranking_df["Student Name"] == selected_student].index[0] + 1
        st.markdown(f"""
        <div style="background-color: #fff3cd; padding: 10px; border-radius: 5px; border-left: 4px solid #ffc107;">
            <strong>📍 {selected_student} is ranked #{current_student_rank} in the class</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Suggestions
        st.subheader("💡 Suggestions for Improvement")
        
        if overall_avg >= 90:
            st.success("🎉 Outstanding performance! Keep maintaining this excellence!")
        elif overall_avg >= 80:
            st.info("✨ Great performance! Continue the good work and aim for higher targets.")
        elif overall_avg >= 70:
            st.warning("⚡ Good performance. Focus on your weaker subjects to improve further.")
        else:
            st.error("🎯 You need to focus more on your studies, especially in weak subjects.")
        
        st.write(f"- **Focus on {weakest}:** This is your weakest subject. Dedicate more time to understanding core concepts.")
        st.write(f"- **Leverage your strength in {strongest}:** Use your proficiency in {strongest} to help you understand similar concepts in other subjects.")
        st.write("- **Consistent study:** Maintain a regular study schedule to ensure steady improvement across all semesters.")
        st.write("- **Seek help:** Don't hesitate to ask teachers or peers for help in subjects where you're struggling.")

if __name__ == "__main__":
    # Example usage
    st.title("Report Card Generator")