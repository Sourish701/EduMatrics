import streamlit as st

# Analysis
def analysis(i, i1, i2, i3):

    st.markdown("## STUDENT PERFORMANCE ANALYSIS (ALL SEMESTERS)")

    # Check if data is valid
    if not i or not i1 or not i2 or not i3:
        st.error("❌ All semester data is required for analysis!")
        return

    # 1. Calculate cumulative totals
    cumulative_totals = {}
    for name in i.keys():
        total = sum(i[name]) + sum(i1[name]) + sum(i2[name]) + sum(i3[name])
        cumulative_totals[name] = total

    # Check if cumulative_totals is empty
    if not cumulative_totals:
        st.error("❌ No student data found!")
        return

    overall_top_student = max(cumulative_totals, key=cumulative_totals.get)
    top_score = cumulative_totals[overall_top_student]

    # Streamlit input instead of input()
    analysis_name = st.text_input("Enter the student's name whose analysis is to be done:")

    if analysis_name:

        if analysis_name in cumulative_totals:

            user_score = cumulative_totals[analysis_name]

            sub_totals = [0, 0, 0, 0, 0]

            # 2. Sum marks across all semesters
            for index in range(5):
                sub_totals[index] = (
                    i[analysis_name][index]
                    + i1[analysis_name][index]
                    + i2[analysis_name][index]
                    + i3[analysis_name][index]
                )

            # 3. Find weakest subject
            min_val = min(sub_totals)
            min_idx = sub_totals.index(min_val)

            subjects_list = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]
            weakest_subject = subjects_list[min_idx]

            st.markdown(f"### Analysis for: **{analysis_name}**")
            st.write(f"Cumulative Total (Sem 1-4): **{user_score}**")
            st.write(f"Overall Top Scorer: **{overall_top_student}** with **{top_score}** marks")

            if analysis_name == overall_top_student:

                st.success(f"Congratulations! {analysis_name} is the top student.")

                st.write(
                    f"Even as the leader, your lowest subject was **{weakest_subject}**. Keep polishing it!"
                )

            else:

                gap = top_score - user_score

                st.warning(
                    f"{analysis_name}, you are currently **{gap} marks** behind the top scorer."
                )

                st.markdown(
                    f"**WEAKNESS IDENTIFIED:** Your lowest scoring subject is **{weakest_subject}**"
                )

                st.write(
                    f"Total points in {weakest_subject} across 4 semesters: **{min_val}**"
                )

                st.markdown("### Suggestions for Improvement")

                st.write(
                    f"- Focus heavily on **{weakest_subject}**; improving this will narrow the **{gap} mark gap**."
                )
                st.write(
                    f"- Review your notes specifically for **{weakest_subject}** from all semesters."
                )
                st.write("- Dedicate an extra hour daily to your weakest subject.")

        else:
            st.error(f"Student name '{analysis_name}' not found.")

    # If only one student
    if len(cumulative_totals) == 1:
        sole_student = list(cumulative_totals.keys())[0]
        st.info(
            f"Only one student ({sole_student}) found in records. No comparative analysis possible."
        )