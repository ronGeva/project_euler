INPUT_PATH = r'ex81_input.txt'

def get_matrix():
	data = open(INPUT_PATH, 'rb').read()
	mat = []
	for line in data.split("\n"):
		if line == '':
			continue
		mat.append([int(num) for num in line.split(",")])

	return mat

def generate_empty_mat(size):
	mat = []
	for i in xrange(size):
		new_list = []
		for j in xrange(size):
			new_list.append(0)
		mat.append(new_list)
	return mat

def set_step_val(row, column, mat, empty_mat):
	below = empty_mat[row + 1][column]
	right = empty_mat[row][column + 1]
	empty_mat[row][column] = min(below, right) + mat[row][column]

def set_borders(mat, empty_mat):
	"""
	sets the values of the borders, (each slot is simply the sum of
	all previous one, starting from [-1][-1] and moving up/left).
	"""
	for row in xrange(len(mat) - 2, -1, -1):
		empty_mat[row][-1] = mat[row][-1] + empty_mat[row + 1][-1]

	for column in xrange(len(mat) - 2, -1, -1):
		empty_mat[-1][column] = mat[-1][column] + empty_mat[-1][column + 1]

def set_mat_values(mat, empty_mat):
	"""
	scans the matrix's diagonlas, first the bottom half of it, and then the
	upper half of it. Sets each slot value as the minimal value to reach it 
	from entry point [-1][-1]
	"""
	row, column = -2, -2
	diagonal_length = 1
	while column >= -len(mat):
		for num in xrange(diagonal_length):
			set_step_val(row - num, column + num, mat, empty_mat)
		column -= 1
		diagonal_length += 1

	diagonal_length -= 1
	column += 1

	while row >= -len(mat):
		for num in xrange(diagonal_length):
			set_step_val(row - num, column + num, mat, empty_mat)
		row -= 1
		diagonal_length -= 1

def calculate_min_path(mat, empty_mat):
	"""
	Sets each item in the empty_mat matrix to be the minimal value
	to reach it from entry point [-1][-1]. Eventually the value
	in empty_mat[0][0] will contain the minimal path's value in
	the entire matrix. (uses dynamic programming)
	"""
	row, column = len(mat) - 1, len(mat) - 1
	empty_mat[row][column] = mat[row][column]
	set_borders(mat, empty_mat)
	set_mat_values(mat, empty_mat)

def main():
	mat = get_matrix()
	empty_mat = generate_empty_mat(80)
	calculate_min_path(mat, empty_mat)
	print "Minimal possible travel value is {0}".format(empty_mat[0][0])


if __name__ == '__main__':
	main()