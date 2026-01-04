from functime1 import flash

def find_highest_per_subject(i, i1, i2, i3):
    print("\n" + "="*40)
    print(f"{'SUBJECT-WISE HIGHEST MARKS SEARCH':^40}")
    print("="*40)

    # 1. Loop for Semester Selection
    sem_prompt = "Enter the semester (1, 2, 3, 4): "
    while True:
        chosen_sem = input(sem_prompt)
        
        if chosen_sem == "1": marks_data = i; break
        elif chosen_sem == "2": marks_data = i1; break
        elif chosen_sem == "3": marks_data = i2; break
        elif chosen_sem == "4": marks_data = i3; break
        else:
            # If invalid, flash error and update the prompt for the next loop
            flash(f"Invalid semester: {chosen_sem}")
            sem_prompt = "Enter semester again (1, 2, 3, 4): "

    # 2. Loop for Subject Selection
    subjects = ["physics", "chemistry", "maths", "computer", "biology"]
    print(f"\nAvailable: {', '.join(subjects)}")
    sub_prompt = "Enter subject name: "
    
    while True:
        chosen_sub = input(sub_prompt).lower()
        
        if chosen_sub in subjects:
            sub_index = subjects.index(chosen_sub)
            break
        else:
            flash(f"Invalid subject: {chosen_sub}")
            sub_prompt = "Enter subject name again: "

    # 3. Calculation Logic (Remains the same)
    max_subject_mark = -1
    top_stud_names = []

    for name, marks_list in marks_data.items():
        current_marks = marks_list[sub_index]
        if current_marks > max_subject_mark:
            max_subject_mark = current_marks
            top_stud_names = [name]
        elif current_marks == max_subject_mark:
            top_stud_names.append(name)

    # 4. Display Result
    print("\n" + "-"*30)
    print(f"RESULT FOR SEMESTER {chosen_sem}")
    print(f"Subject: {chosen_sub.capitalize()}")
    print(f"Highest Marks: {max_subject_mark}")
    print(f"Received by: {', '.join(top_stud_names)}")
    print("-"*30)