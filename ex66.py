from pe_useful import get_all_squares, binary_search

def find_smallest_d(d_limit, squares_limit):
	"""
	according to Diophantine equation:
	x^2 - d * y^2 = 1, there will be exactly 0 solution to the equation
	in case d is a square as well. Therefore we will skip squares during
	our calculations.

	The function finds d that yields the biggest possible x for the smallest
	possible y that answers Diophantine equation.
	"""
	best_d = -1
	biggest_x = 0
	squares = get_all_squares(squares_limit + 1)
	for d in xrange(2, d_limit + 1):
		if binary_search(squares, d) != -1:
			continue #in case d is a square

		found_flag = False
		for y in xrange(2, squares_limit):
			curr_x = squares[y] * d + 1
			if binary_search(squares, curr_x) != -1:
				if curr_x > biggest_x:
					print "Found a better d! {0} > {1}. d = {2}".format(curr_x, biggest_x, d)
					best_d = d
					biggest_x = curr_x
				found_flag = True
				break
		if not found_flag:
			print "couldn't find a solution for d = {0}".format(d)

	return best_d, biggest_x

def main():
	print find_smallest_d(1000, 10000000)

if __name__ == '__main__':
	main()