import sys

original = sys.argv[1]
short = ""
count = 1
letter = ""

for i in range(0, int(len(original))):
    if letter != original[i]:
        letter = original[i]
        if count != 1:
            short += str(count)
        short += letter
        count = 1
    else:
        count += 1

if count != 1:
    short += str(count)

if int(len(short)) < int(len(original)):
    print(short)
else:
    print(original)
