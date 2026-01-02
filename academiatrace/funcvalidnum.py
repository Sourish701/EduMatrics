def get_valid_num_students():
    from functime1 import flash
    
    # The prompt starts as the subject name
    prompt = f"Enter number of students: "
    
    while True:
        # ONLY ONE INPUT CALL HERE
        user_in = input(prompt)
        
        try:
            m = int(user_in)
            if m<=0:
                flash("Invalid amount! Number of students must be greater than zero.")
                prompt = "Please enter number of students again: "
                
            if m > 0:
                return m
                
        except ValueError:
            # Not a number (letters/symbols)
            flash("Invalid amount! Please enter numeric values only.")
            prompt = "Please enter number of students again: "            