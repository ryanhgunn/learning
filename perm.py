# A script to tell if two strings are permutations of one another.

import sys

string1 = input("First string? ")
string2 = input("Second string? ")

if len(string1) != len(string2):
    print("Strings are different lengths and cannot be permutations.")
    sys.exit(0)
else:
    for i in range(0, len(string1)):
        if string1 == string2:
            print("Strings are permutations.")
            sys.exit(0)
        else:
            string1 = string1[1:] + string1[1]

print("Strings are not permutations.")
