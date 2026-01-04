import time
def flash(message):
    print(message,end="",flush=True)
    time.sleep(2)
    print("\r"+" "*len(message)+"\r",end="",flush=True)
    
    print("\033[F\033[K", end="", flush=True)