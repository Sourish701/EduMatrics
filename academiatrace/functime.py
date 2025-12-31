import time
def get_clean_input():
    while True:
        user_input = input("Enter a number: ")
        
        if user_input.isdigit():
            # If correct, we keep it and break
            print(f"Success! You entered: {user_input}")
            break
        else:
            # If wrong, wait a second so they see the error
            print("Invalid entry! Try again...", end="", flush=True)
            time.sleep(1)
            
            # THE TRICK:
            # 1. Move up 1 line (to the 'Invalid entry' line) and clear it
            # 2. Move up another line (to the user's input line) and clear it
            print("\033[1A\033[K" + "\033[1A\033[K", end="", flush=True)

get_clean_input()