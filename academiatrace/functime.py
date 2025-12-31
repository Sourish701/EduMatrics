import time
def flash_and_input(message,prompt):
    print(message,end="",flush=True)
    time.sleep(2)
    print("\r"+" "*len(message)+"\r",end="",flush=True)
    print("\033[1A\033[K" + "\033[1A\033[K", end="", flush=True)
    return input(prompt)        