import sys

Left = [i for i in range(int(sys.argv[1]), 0, -1)]
Middle = []
Right = []

counter = 0

def show():
	global counter
	print(str(counter) + ":", Left, Middle, Right)

def move(initial, target):
	global counter
	if  len(initial) == 0 or (len(target)>0 and initial[-1] > target[-1]):
		print("Error, invalid move.")
		sys.exit(0)
	last = initial.pop()
	target.append(last)
	counter += 1
	show()

show()

def solve(number, initial, target, spare):
	if number > 1:
		solve(number - 1, initial, spare, target)
		move(initial, target)
		solve(number - 1, spare, target, initial)
	else:
		move(initial, target)

solve(int(sys.argv[1]), Left, Right, Middle)
