# A script to determine if characters in a given string are unique.

import sys

string = input("Input a string here: ")

for i in range(0, len(string)):
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            print("The characters in the given string are not unique.")
            sys.exit(0)

print("The characters in the given string are unique.")
