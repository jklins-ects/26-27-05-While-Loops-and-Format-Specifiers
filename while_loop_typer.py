import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Call the function whenever you need it
mystr = ""
while (mystr == ""):
    mystr = input("Enter a string for me to type back out: ").strip()
# note: A for loop will be better for this, but we're looking at string indexing

# print("line 1\nline 2\nline 3") #\n newline - advance to the next line

index = 0
clear_screen()
while index < len(mystr):
    print(mystr[index], end="", flush=True)  # by default, end is a \n
    time.sleep(.2)
    index += 1
