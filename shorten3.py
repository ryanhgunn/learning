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

# if we have a new letter, finish counting for the old letter and
# add its counter to the string (if not 1). then, add the new letter
# to our string and reset the counter.

    else:
        count += 1

# otherwise, increment the counter.

if count != 1:
    short += str(count)

# upon ending the for loop, add the last letter's counter to the end
# if it is not 1.

if int(len(short)) < int(len(original)):
    print(short)
else:
    print(original)

# check that the shortened string is shorter than the original and
# print the shorter version.
