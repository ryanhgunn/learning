sequence = [0, 1]

for i in range(0, 1000):
	sequence.append(sequence[i] + sequence[i +1])
print(sequence)
