def get_valid_names():
    while True:
        m = input(f"Enter your name: ")
        if not m.isalpha():
            from functime import flash_and_input
            user_input=flash_and_input("Invalid name!(Please enter alphabets only)","Please enter name again: ")
            return user_input
        else:
            return m
        
        
    exit