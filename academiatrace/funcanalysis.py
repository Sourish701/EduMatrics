#Analysis
def analysis(i, i1, i2, i3):
   
    print("\n" + "="*50)
    print("STUDENT PERFORMANCE ANALYSIS (ALL SEMESTERS)")
    print("="*50)

# 1. Calculate cumulative totals (Same as your logic)
    cumulative_totals = {}
    for name in i.keys():
        total = sum(i[name]) + sum(i1[name]) + sum(i2[name]) + sum(i3[name])
        cumulative_totals[name] = total

    overall_top_student = max(cumulative_totals, key=cumulative_totals.get)
    top_score = cumulative_totals[overall_top_student]

    analysis_name = input("Enter the student's name whose analysis is to be done: ")

    if analysis_name in cumulative_totals:
        user_score = cumulative_totals[analysis_name]
    
   
        sub_totals = [0, 0, 0, 0, 0]
    
# 2. Sum marks across all 4 sem dictionaries (i, i1, i2, i3)
        for index in range(5):
            sub_totals[index] = i[analysis_name][index] + i1[analysis_name][index] + \
                            i2[analysis_name][index] + i3[analysis_name][index]
    
# 3. Find the subject with the minimum total
        min_val = min(sub_totals)
        min_idx = sub_totals.index(min_val)
        subjects_list = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]
        weakest_subject = subjects_list[min_idx]
   
        print(f"\nAnalysis for: {analysis_name}")
        print(f"Cumulative Total (Sem 1-4): {user_score}")
        print(f"Overall Top Scorer: {overall_top_student} with {top_score} marks")
    
        if analysis_name == overall_top_student:
            print(f"\nREMARKS: Congratulations! {analysis_name} is the top student.")
            print(f"Even as the leader, your lowest subject was {weakest_subject}. Keep polishing it!")
        else:
            gap = top_score - user_score
            print(f"\nREMARKS: {analysis_name}, you are currently {gap} marks behind the top scorer.")
        
# 4. Specific Lowest Subject Remark
            print(f"**WEAKNESS IDENTIFIED:** Your lowest scoring subject is **{weakest_subject}**.")
            print(f"Total points in {weakest_subject} across 4 semesters: {min_val}")
        
            print("\nSUGGESTIONS FOR IMPROVEMENT:")
            print(f"* Focus heavily on **{weakest_subject}**; improving this will narrow the {gap} mark gap.")
            print(f"* Review your notes specifically for {weakest_subject} from all semesters.")
            print("* Dedicate an extra hour daily to your weakest subject.")
    else:
        print(f"Error: Student name '{analysis_name}' not found.")
# 5. If there is only one student, handle that case
    if len(cumulative_totals) == 1:
        sole_student = list(cumulative_totals.keys())[0]
        print(f"\nNOTE: Only one student ({sole_student}) found in records. No comparative analysis possible.")        