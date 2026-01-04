import time

def flash_and_input(message, prompt):
    # 1. Print the error message
    print(message, end="", flush=True)
    time.sleep(1.5)
    
    # 2. Clear the error message line (The current line)
    print("\r" + " " * len(message) + "\r", end="", flush=True)
    
    # 3. Move the cursor up and clear that line too
    print("\033[F\033[K", end="", flush=True)
    
    # 4. Return the new input prompt
    return input(prompt)