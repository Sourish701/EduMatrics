def get_valid_marks(subject_name):
    from functime1 import flash
    
    # The prompt starts as the subject name
    prompt = f"Enter marks in {subject_name} "
    
    while True:
        # ONLY ONE INPUT CALL HERE
        user_in = input(prompt)
        
        try:
            m = int(user_in)
            if 0 <= m <= 100:
                return m
            else:
                # Number out of range
                flash("Invalid marks! Please enter marks between 0 and 100.")
                prompt = "Please enter marks in {subject_name} again: "
                
        except ValueError:
            # Not a number (letters/symbols)
            flash("Invalid marks! Please enter numeric values only.")
            prompt = "Please enter marks in {subject_name} again: "
           