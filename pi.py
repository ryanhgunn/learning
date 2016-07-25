import sys

approximation = 0

for i in range(0, int(sys.argv[1])):
	approximation = approximation + (((-1)**i)/(2*i + 1))
	print (4*approximation)
