import sys

orig = sys.argv[1]
short = ""
count = 1
letter = ""

for i in range(0, int(len(orig))):
	if letter != orig[i]:
		letter = orig[i]
		if count != 1:
			short += str(count)
		short += letter
		count = 1
	else:
		count += 1

if count != 1:
	short += str(count)

if int(len(short)) < int(len(orig):
	print(short)
else:
	print(orig)
