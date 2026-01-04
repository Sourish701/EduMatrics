def get_valid_names():
    from functime1 import flash
    
    # Start with the standard prompt
    prompt = "Enter your name: "
    
    while True:
        m = input(prompt)
        
        # .isalpha() checks if the string contains ONLY letters
        if m.isalpha():
            return m 
        else:
          
            flash("Invalid name! (Alphabets only)")
            prompt = "Please enter your name again: "