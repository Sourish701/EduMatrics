# Finding the highest in 1st Sem
def highest_in_1stsem(i):
    if not i: # Check if dictionary is empty to prevent errors
        print("No data found for 1st Semester.")
        return
    max_total_marks = -1
    top_student_name = ""
    for name, marks in i.items():
        total_marks = sum(marks)
        if total_marks > max_total_marks:
            max_total_marks = total_marks
            top_student_name = name
    print(f"\nThe highest total marks in 1st Sem: {max_total_marks} was received by: {top_student_name}")

# Finding the highest in 2nd Sem
def highest_in_2ndsem(i1):
    if not i1:
        print("No data found for 2nd Semester.")
        return
    max_total_marks = -1
    top_student_name = ""
    for name, marks in i1.items():
        total_marks = sum(marks)
        if total_marks > max_total_marks:
            max_total_marks = total_marks
            top_student_name = name
    print(f"\nThe highest total marks in 2nd Sem: {max_total_marks} was received by: {top_student_name}")

# Finding the highest in 3rd Sem
def highest_in_3rdsem(i2):
    max_total_marks = -1
    top_student_name = ""
    for name, marks in i2.items():
        total_marks = sum(marks)
        if total_marks > max_total_marks:
            max_total_marks = total_marks
            top_student_name = name
    print(f"\nThe highest total marks in 3rd Sem: {max_total_marks} was received by: {top_student_name}")

# Finding the highest in 4th Sem
def highest_in_4thsem(i3):
    max_total_marks = -1
    top_student_name = ""
    for name, marks in i3.items():
        total_marks = sum(marks)
        if total_marks > max_total_marks:
            max_total_marks = total_marks
            top_student_name = name
    print(f"\nThe highest total marks in 4th Sem:  {max_total_marks} was received by: {top_student_name}")

