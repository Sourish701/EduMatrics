from funcvalidmark import get_valid_marks
from funcvalidname import get_valid_names
from funcvalidnum import get_valid_num_students 
from functime import flash_and_input
from funcyn import get_yes_no

def sem_marks():
    n = get_valid_num_students()
    
    # --- SEMESTER 1 ---
    i = {}
    s = []
    k = 0
    for x in range(n):
        print(f"\n--- Entering marks for (1st Sem) ---")
        name = get_valid_names()
        marks = [get_valid_marks("physics "), get_valid_marks("chemistry "), 
                 get_valid_marks("maths "), get_valid_marks("computer "), 
                 get_valid_marks("biology ")]
        i[name] = marks

    # Memory variable to track the student searched
    last_target = None 

    ch = get_yes_no("\nDo you want to find average for 1st sem? (y/n): ")
    if ch == 'y':
        search = input("Whose average marks do you want to find?: ")
        if search not in i:
            search = flash_and_input("Invalid student name!", "Enter name again: ")
        
        if search in i:
            avg = sum(i[search]) / 5
            print(f"Average marks for 1st sem of {search} is {avg}")
            last_target = search # Store in memory
        else:
            print(f"Sorry, {search} not found.")

    # --- SEMESTER 2 ---
    i1 = {}
    for name in i.keys():
        print(f"\n--- Entering marks for {name} (2nd Sem) ---")
        marks = [get_valid_marks("physics "), get_valid_marks("chemistry "), 
                 get_valid_marks("maths "), get_valid_marks("computer "), 
                 get_valid_marks("biology ")]
        i1[name] = marks

    ch2 = get_yes_no("\nDo you want to find average for 2nd sem? (y/n): ")
    if ch2 == 'y':
        # Check if memory exists
        if last_target:
            reuse = get_yes_no(f"Find average for same student ({last_target})? (y/n): ")
            if reuse == 'y':
                current_target = last_target
            else:
                current_target = input("Enter new student name: ")
        else:
            current_target = input("Enter student name: ")

        if current_target in i1:
            print(f"Average for 2nd sem of {current_target} is {sum(i1[current_target])/5}")
            last_target = current_target # Update memory
        else:
            print("Record not found.")

    # --- SEMESTER 3 ---
    i2 = {}
    for name in i.keys():
        print(f"\n--- Entering marks for {name} (3rd Sem) ---")
        i2[name] = [get_valid_marks("physics "), get_valid_marks("chemistry "), 
                    get_valid_marks("maths "), get_valid_marks("computer "), 
                    get_valid_marks("biology ")]

    ch3 = get_yes_no("\nDo you want to find average for 3rd sem? (y/n): ")
    if ch3 == 'y':
        if last_target:
            reuse = get_yes_no(f"Find average for same student ({last_target})? (y/n): ")
            current_target = last_target if reuse == 'y' else input("Enter new student name: ")
        else:
            current_target = input("Enter student name: ")

        if current_target in i2:
            print(f"Average for 3rd sem of {current_target} is {sum(i2[current_target])/5}")
            last_target = current_target
        else:
            print("Record not found.")

    # --- SEMESTER 4 ---
    i3 = {}
    for name in i.keys():
        print(f"\n--- Entering marks for {name} (4th Sem) ---")
        i3[name] = [get_valid_marks("physics "), get_valid_marks("chemistry "), 
                    get_valid_marks("maths "), get_valid_marks("computer "), 
                    get_valid_marks("biology ")]

    ch4 = get_yes_no("\nDo you want to find average for 4th sem? (y/n): ")
    if ch4 == 'y':
        if last_target:
            reuse = get_yes_no(f"Find average for same student ({last_target})? (y/n): ")
            current_target = last_target if reuse == 'y' else input("Enter new student name: ")
        else:
            current_target = input("Enter student name: ")

        if current_target in i3:
            print(f"Average for 4th sem of {current_target} is {sum(i3[current_target])/5}")
            last_target = current_target
        else:
            print("Record not found.")

    return i, i1, i2, i3