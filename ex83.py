"""
This problem is a classic path finding exercise in a 80X80 matrix where we need to reach the bottom-right cell from the
top-left cell going through cells whose sum is the smallest.
The trivial solution would be to try every possible turn until we reach the bottom-right cell, which would run in
O(4^n), obviously unfeasible for n=80.

The method attempted here to solve this problem is using dynamic programming, going from the end of the path (the
bottom-right cell, upwards towards the top-left cell).
We scan the matrix in diagonals, find the minimal path for each cell in the diagonal (based on its right and bottom
cells), and then fix all the paths of the adjacent cells affected by this change (recursively).

Note we set all cells values to INFINITE initially, so that we won't attempt to resursively update the entire matrix
in our first run, and instead stop whenever we reach cells we have yet to scan digonally. This way we assure the best
routes to the end cell have already been calculate for a smaller matrix, and we only have to perform minor fixes for
each new cell scanned, resulting in total complexity of O(n^2 * 4n^2) = O(4n^4) = O(n^4), when our matrix is sized n * n
For ex83, this means we perform roughly 80^4 = 40 millions calculations, which is great :)
"""

from pe_useful import load_matrix_from_file
DATA_FILEPATH = 'ex83_input.txt'  # the file containing the matrix data
INFINITE = float('inf')


class Cell(object):
	def __init__(self, value=INFINITE, path_value=INFINITE):
		self.value = value
		self.min_path_value = path_value


class Matrix(object):
	def __init__(self, table_values):
		self._rows = []
		self._rows = [[Cell() for col in xrange(len(row))] for row in table_values]
		self._rows[-1][-1].min_path_value = table_values[-1][-1]
		self._rows[-1][-1].value = table_values[-1][-1]
		self._original_values = table_values

	def _in_matrix(self, row_index, column_index):
		return 0 <= row_index < len(self._rows) and 0 <= column_index < len(self._rows[0])

	def _update_neighbor_if_in_matrix(self, row_index, column_index, possible_min_path):
		if self._in_matrix(row_index, column_index):
			self._update_cell_min_path(row_index, column_index,
									   self._rows[row_index][column_index].value + possible_min_path)

	def _update_cell_min_path(self, row_index, column_index, new_min_path):
		"""
		Possibly updates the min_path_value of a single cell, and in case a change was made calls recursively this
		method for all the cells affected by the change, the cell to its right and the cell to its left (which of
		course recursively updates the cells affected by them, which will end up eventually covering all the cells whose
		diagonal is to the right of this cell's diagonal).
		:param row_index: The index of the row of the cell.
		:param column_index: The index of the column of the cell.
		:param new_min_path: The new possible minimal path from the cell to the bottom-right cell found.
		:return: None
		"""
		cell = self._rows[row_index][column_index]
		if new_min_path >= cell.min_path_value:
			return

		cell.min_path_value = new_min_path
		self._update_neighbor_if_in_matrix(row_index + 1, column_index, new_min_path)
		self._update_neighbor_if_in_matrix(row_index, column_index + 1, new_min_path)
		self._update_neighbor_if_in_matrix(row_index - 1, column_index, new_min_path)
		self._update_neighbor_if_in_matrix(row_index, column_index - 1, new_min_path)

	def _get_possible_min_path_for_cell(self, cell_row, cell_col):
		"""
		Retrieves the smallest of the two paths possible for the cell - through the bottom cell and through the left
		cell.
		"""
		if self._in_matrix(cell_row + 1, cell_col):
			bottom_value = self._rows[cell_row + 1][cell_col].min_path_value
		else:
			bottom_value = INFINITE
		if self._in_matrix(cell_row, cell_col + 1):
			right_value = self._rows[cell_row][cell_col + 1].min_path_value
		else:
			right_value = INFINITE
		return min(bottom_value, right_value)

	def _update_diagonal_paths(self, row_index, column_index):
		"""
		Updates the min_path_value of the cells in the diagonal given as an argument.
		:param row_index: The row index of the bottom left cell in the diagonal.
		:param column_index: The column index of the bottom left cell in the diagonal.
		:return: None
		"""
		while self._in_matrix(row_index, column_index):
			# Set the value only here to prevent attempting to access cells to our right/up
			self._rows[row_index][column_index].value = self._original_values[row_index][column_index]
			possible_min_path = self._get_possible_min_path_for_cell(row_index, column_index)
			self._update_cell_min_path(row_index, column_index,
									   possible_min_path + self._rows[row_index][column_index].value)
			column_index += 1
			row_index -= 1

	def calculate_minimal_paths(self):
		"""
		Searches for the minimal sum of cells that get us from the top-left cell to the bottom-right cell.
		:return: None
		"""
		bottom_row_indexes = [(len(self._rows) - 1, col) for col in xrange(len(self._rows[0]))]
		left_col_indexes = [(row_index, 0) for row_index in xrange(len(self._rows))]

		for index in bottom_row_indexes[::-1]:
			self._update_diagonal_paths(*index)

		for index in left_col_indexes[-2::-1]:
			self._update_diagonal_paths(*index)

	def get_minimal_path(self):
		return self._rows[0][0].min_path_value


def main():
	table = load_matrix_from_file(DATA_FILEPATH)
	matrix = Matrix(table)
	matrix.calculate_minimal_paths()
	print matrix.get_minimal_path()


main()
