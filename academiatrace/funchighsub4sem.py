def show_overall_subject_toppers(i, i1, i2, i3):
    subjects = ["Physics", "Chemistry", "Maths", "Computer", "Biology"]
    # Get all student names from the first semester
    student_names = list(i.keys())
    
    print("\n" + "="*55)
    print(f"{'OVERALL SUBJECT TOPPERS (SEM 1-4)':^55}")
    print("="*55)
    print(f"{'Subject':<15} | {'Topper(s)':<25} | {'Total'}")
    print("-" * 55)

   
    for index in range(len(subjects)):
        max_total_mark = -1
        toppers = []

        for name in student_names:
            
            total_subject_mark = i[name][index] + i1[name][index] + \
                                 i2[name][index] + i3[name][index]
            
            if total_subject_mark > max_total_mark:
                max_total_mark = total_subject_mark
                toppers = [name]
            elif total_subject_mark == max_total_mark:
                toppers.append(name)

        topper_names = ", ".join(toppers)
       
        print(f"{subjects[index]:<15} | {topper_names:<25} | {max_total_mark}/400")