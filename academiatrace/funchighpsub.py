#For finding the highest marks received in a semester by a student as per chosen by the user
def find_highest_per_subject(i, i1, i2, i3): # Receives all dictionaries
    print("\n----- Subject-wise Highest Marks Search -----")
    chosen_sem = input("Enter the semester (1, 2, 3, 4): ")
    
    # 1. Map chosen_sem to the correct dictionary
    marks_data = None
    if chosen_sem == "1": marks_data = i
    elif chosen_sem == "2": marks_data = i1
    elif chosen_sem == "3": marks_data = i2
    elif chosen_sem == "4": marks_data = i3
    
    if marks_data is None:
        print(f"Invalid semester: {chosen_sem}")
        return

    # 2. Handle Subject Input
    subjects = ["physics", "chemistry", "maths", "computer", "biology"]
    print(f"Available subjects: {', '.join(subjects)}")
    chosen_sub = input("Enter subject name: ").lower()

    if chosen_sub not in subjects:
        print(f"Invalid subject: {chosen_sub}")
        return
    
    sub_index = subjects.index(chosen_sub)

    # 3. Calculation Logic
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
    print(f"\nResult for Semester {chosen_sem}:")
    print(f"Subject: {chosen_sub.capitalize()}")
    print(f"Highest Marks: {max_subject_mark}")
    print(f"Received by: {', '.join(top_stud_names)}")
    print(f"---------------------------------------------")