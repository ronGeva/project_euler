"""
The problem is easily solved using dynamic programing,
we'll need to find the best route the fastest way possible, 
counting all possible routes will take literally forever so our
best option is to calculate the best route backwards.
We'll compare every 2 adjacent numbers to see which one is bigger
and add it to the number leading to them. This way when we'll
reach the first row we'll only have 2 numbers left that will contain
the largest sums of all the numbers in the input, then, the bigger one
will be chosen.
"""

INPUT_PATH = "ex67_input.txt"

def get_input():
	data = ""
	with open(INPUT_PATH, "rb") as f:
		data = f.read()

	input_data = []
	for line in data.split("\n"):
		line = line.split(" ")
		if "" in line:
			line.remove("")
		input_data.append([int(num) for num in line])

	if [] in input_data:
		input_data.remove([])
	return input_data

def calculate_prev_level(curr_level_index, data):
	for i in xrange(curr_level_index):
		try:
			data[curr_level_index - 1][i] += max(data[curr_level_index][i],
				 data[curr_level_index][i + 1])
		except:
			print "curr_level_index : {0}, i : {1}".format(curr_level_index, i)

def calculate_maximum_route(data):
	for curr_level in xrange(len(data) - 1, 0, -1):
		calculate_prev_level(curr_level, data)

	return data[0][0]

def test():
	input_data = get_input()
	print calculate_maximum_route(input_data)

if __name__ == '__main__':
	test()