OPS = ['+', '-', '*', '/']

def get_singular_show_sets(curr_set, remaining_options):
	"""
	Finds all the sets of numbers possible that contain the curr_set +
	all the possible combination of the numbers in remaining options (when each
	number in it only appears once)
	:return: a list containing all the sets as mentioned
	"""
	if len(remaining_options) == 1:
		return curr_set + remaining_options

	sets = []
	for option in remaining_options:
		new_curr_set = curr_set + [option]
		new_remaining_options = list(remaining_options)
		new_remaining_options.remove(option)
		new_sets = get_singular_show_sets(new_curr_set, new_remaining_options)
		if isinstance(new_sets[0], list):
			sets += new_sets
		else:
			sets.append(sets)

	return sets

def get_repeating_show_sets(curr_set, options, set_size):
	"""
	Similiar to get_singular_show_sets, except each option in options can
	appear more than once in the set. The amount of numbers in each set
	will be equal to set_size.
	"""
	if len(curr_set) == 4:
		return curr_set

	sets = []
	for option in options:
		new_sets = get_repeating_show_sets(curr_set + [option], options, set_size)
		if isinstance(new_sets[0], list):
			sets += new_sets
		else:
			sets.append(new_sets)
	return sets

def calculate_value(numbers, priority, operators):
	"""
	Calculate the value of the given equation, when each arithmetic action will
	be done in the order determined by the priority list, using the numbers at its
	index and its index + 1.
	In case an illegal arithmetic action is performed, returns None.
	:param numbers: a list containing 4 integers.
	:param priority: a list containing the numbers 0, 1 and 2, not necessarily in this
	order. Determines the order in which we'll perform the arithmetic operators on the
	numbers.
	:param operators: a list containing 3 operators that determine the arithmetic action
	that will be used on the 2 numbers at current operator's index with the number at the
	current operator's index + 1.
	:return: An integer representing the value of the equation.
	"""
	pass

def get_all_values(numbers, operators):
	"""
	Finds all the different values that we can find by applying the operators given to us
	in any possible order.
	:param numbers: a list containing 4 integers.
	:param operators: a list containing 3 chars representing arithmetic operators.
	:return: a list as described above, without any repeating values, without None and without
	0.
	"""
	pass

def get_amount_of_consecutive_numbers(set_of_nums):
	"""
	Returns the amount of consecutive numbers from 1.
	:param set_of_nums: a list of all the numbers achieved using calculate_value on a given
	list of numbers with all possible operators and in all the possible orders.
	:return: an integer.
	"""
	pass

def get_all_numbers():
	"""
	:return: a list containing all possible tuples of a,b,c,d when all of those are single digits
	and a<b<c<d.
	"""
	numbers = []
	for a in xrange(1, 7):
		for b in xrange(2, 8):
			for c in xrange(3, 9):
				for d in xrange(4, 10):
					numbers.append((a, b, c, d))
	return numbers

def find_longest_consecutive_set():
	"""
	Finds the 4 numbers a<b<c<d that form a list containing the longest chain of consecutive
	integers when we perform every possible set of operators on them in all possible orders.
	:return:
	"""
	pass

def test():
	ops = get_repeating_show_sets([], OPS, 4)
	numbers = get_singular_show_sets([], [1,2,3,4])
	print len(numbers)

test()
