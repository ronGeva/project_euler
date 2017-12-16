from pe_useful import binary_search, test_func, save_progress, load_progress
import math, progressbar, signal, sys, json

AMOUNT_OF_SQUARES = 10000000

def get_squares(num_limit):
	"""
	returns a list containing all squares of numbers up to num_limit - 1.
	complexity: O(num_limit^2)
	"""
	squares = []
	for num in xrange(num_limit):
		squares.append(pow(num, 2))

	return squares

def is_diphontine_equation(d, num, squares):
	"""
	Checks if the equation X^2 = d * num^2 + 1 is true.
	"""
	num_squared = squares[num]
	possible_square = num_squared * d + 1
	return binary_search(squares, possible_square) != -1

def get_vars():
	args = load_progress('ex75')
	if len(args) == 0:
		return (2, 0, [])

	else:
		return args

def find_biggest_minimal_d(d_limit, squares):
	biggest_minimal_d, biggest_square = get_vars()

	def close_program(signal, frame):
		args = [biggest_minimal_d, biggest_square]
		save_progress(args, 'ex75')
		sys.exit(0)

	signal.signal(signal.SIGINT, close_program)

	bar = progressbar.ProgressBar()
	for d in bar(xrange(biggest_minimal_d, d_limit)):
		num = 2
		found_num = False
		while num < len(squares) and not found_num:
			if is_diphontine_equation(d, num, squares):
				created_square = squares[num] * d + 1
				if created_square > biggest_square:
					biggest_square = created_square
					biggest_minimal_d = d
				found_num = True
			num += 1
		if not found_num:
			print "couldn't found num for {0}".format(d)

	return biggest_minimal_d, biggest_square, unexplored_ds

@test_func
def main():
	print "searching for the first {0} squares!".format(AMOUNT_OF_SQUARES)
	squares = get_squares(AMOUNT_OF_SQUARES)
	print "finished retrieving the squares. now finding d that will yield the biggest minimal x."
	print find_biggest_minimal_d(1000, squares)

if __name__ == '__main__':
	main()