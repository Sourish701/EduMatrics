from functime1 import flash
def get_yes_no(prompt_text):
    prompt = prompt_text
    while True:
        choice = input(prompt).lower().strip()
        if choice in ['y', 'n']:
            return choice
        else:
            flash("Invalid input! (Please enter 'y' or 'n')")
            prompt = "Enter your choice again (y/n): "