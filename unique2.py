# A script to tell if characters in a given string are unique, alternate approach.

import sys

string = input("Input a string here: ")
characters = []

for i in range(0, len(string)):
    if string[i] in characters:
        print("The characters in the given string are not unique.")
        sys.exit(0)
    else:
        characters.append(string[i])

print("The characters in the given string are unique.")
