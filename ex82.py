from copy import deepcopy

DATA_PATH = "C:\Users\Geva\Desktop\Ron\code\pe\ex82_input.txt"


class Matrix(object):
	def __init__(self, orig_table):
		self.original_vals_table = deepcopy(orig_table)
		self.curr_val_table = deepcopy(orig_table)
		self.initiate_matrix()

	def set_cell_val(self, row, col):
		"""
		Sets the value of the current cell (determined by row and col parameters) to the
		minimal value possible for it (determining it by checking what's the cheapest step
		forward + its base val from the original_vals table
		:return: None
		"""
		if col == len(self.original_vals_table) - 1:
			return

		base_val = self.original_vals_table[row][col]
		min_val = self.curr_val_table[row][col + 1]
		min_val = self.find_minimal_val(min_val, col, xrange(row - 1, -1, -1))
		min_val = self.find_minimal_val(min_val, col, xrange(row + 1, len(self.curr_val_table)))

		self.curr_val_table[row][col] = min_val + base_val

	def find_minimal_val(self, min_val, col, curr_range):
		"""
		Returns the minimal value possible for us to reach the current column
		from within the given range (curr_range). Relative to min_val (which
		represents the current minimal value found for the value of this cell).
		:return: The minimal value found in the given range.
		"""
		stacking_value = 0
		for possible_row in curr_range:
			stacking_value += self.original_vals_table[possible_row][col]
			current_possible_val = stacking_value + self.curr_val_table[possible_row][col + 1]
			if min_val > current_possible_val:
				min_val = current_possible_val

		return min_val

	def initiate_matrix(self):
		"""
		Initiates the matrix. Runs on every cell (from the last column to the first),
		and sets its value.
		:return:
		"""
		for col in xrange(len(self.original_vals_table) - 1, -1, -1):
			for row in xrange(len(self.original_vals_table)):
				self.set_cell_val(row, col)

	@property
	def min(self):
		"""
		The value of the minimal path found from one side of the matrix to the other.
		"""
		return min([vals[0] for vals in self.curr_val_table])


def get_table():
	"""
	:return: a table containing the data required for this problem.
	"""
	with open(DATA_PATH, 'rb') as f:
		data = f.read()

	table = []
	for line in data.split("\n"):
		if line != '':
			line = [int(num) for num in line.split(",")]
			table.append(line)

	return table


def main():
	table = get_table()
	matrix = Matrix(table)
	print 'Minimal route is {0}'.format(matrix.min)


if __name__ == '__main__':
	main()