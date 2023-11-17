import sys
import os

def clear_screen():
    if sys.platform.startswith("win32"):
        os.system("cls")
    else:
        os.system("clear")
