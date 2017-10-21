def calc_maximum_path(mat, line_index, col_index):

	if line_index == len(mat) - 1:
		return mat[line_index][col_index]

	left_maximum = calc_maximum_path(mat, line_index + 1, col_index)
	right_maximum = calc_maximum_path(mat, line_index + 1, col_index + 1)

	return max(left_maximum, right_maximum) + mat[line_index][col_index]


def generate_mat(input_data):
	mat = []
	for line in input_data.split("\r\n"):
		new_line = []
		for num in line.split(" "):
			new_line.append(int(num))
		mat.append(new_line)

	return mat

def main():
	input_data = open('ex18_input.txt', 'rb').read()
	mat = generate_mat(input_data)
	for line in mat:
		print line

	maximum_path = calc_maximum_path(mat, 0, 0)
	print "maximum path is {0}".format(maximum_path)

if __name__ == '__main__':
	main()