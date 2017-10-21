MAT_SIZE = 20

def is_right_count_possible(col_index):
	return col_index <= MAT_SIZE - 4

def is_down_count_possible(line_index):
	return line_index <= MAT_SIZE - 4

def is_up_count_possible(line_index):
	return line_index >= 3

def get_biggest_val(mat, line_index, col_index):
	possible_vals = []

	if is_right_count_possible(col_index):
		right_val = 1
		for i in xrange(4):
			right_val *= mat[line_index][col_index + i]
		possible_vals.append(right_val)

	if is_down_count_possible(line_index):
		down_val = 1
		for i in xrange(4):
			down_val *= mat[line_index + i][col_index]
		possible_vals.append(down_val)

	if is_down_count_possible(line_index) and is_right_count_possible(col_index):
		down_diagonal = 1
		for i in xrange(4):
			down_diagonal *= mat[line_index + i][col_index + i]
		possible_vals.append(down_diagonal)

	if is_up_count_possible(line_index) and is_right_count_possible(col_index):
		up_diagonal = 1
		for i in xrange(4):
			up_diagonal *= mat[line_index - i][col_index + i]
		possible_vals.append(up_diagonal)

	if len(possible_vals) == 0:
		return 0

	return max(possible_vals)

def get_biggest_val_in_mat(mat):
	biggest_val = 0
	for line_index in xrange(MAT_SIZE):
		for col_index in xrange(MAT_SIZE):
			curr_val = get_biggest_val(mat, line_index, col_index)
			if curr_val > biggest_val:
				biggest_val = curr_val

	return biggest_val

def generate_mat(input_data):
	mat = []
	for line in input_data.split("\r\n"):
		new_line = []
		for num in line.split(" "):
			new_line.append(int(num))
		mat.append(new_line)
	return mat

def main():
	input_data = open(r'C:\Users\Geva\Desktop\Ron\code\PE\ex11_input.txt', 'rb').read()
	mat = generate_mat(input_data)
	for line in mat:
		print line

	biggest_val = get_biggest_val_in_mat(mat)
	print "Biggest multiplication of 4 adjacent numbers is {0}".format(biggest_val)


if __name__ == '__main__':
	main()