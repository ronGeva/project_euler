from progressbar import ProgressBar

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
			sets.append(new_sets)

	return sets


def get_repeating_show_sets(curr_set, options, set_size):
	"""
	Similiar to get_singular_show_sets, except each option in options can
	appear more than once in the set. The amount of numbers in each set
	will be equal to set_size.
	"""
	if len(curr_set) == set_size:
		return curr_set

	sets = []
	for option in options:
		new_sets = get_repeating_show_sets(curr_set + [option], options, set_size)
		if isinstance(new_sets[0], list):
			sets += new_sets
		else:
			sets.append(new_sets)
	return sets


def calculate_single_op(numbers, operator):
	"""
	Returns the value of numbers[0] <operator> numbers[1]
	"""
	try:
		if operator == '+':
			return numbers[0] + numbers[1]
		if operator == '-':
			return numbers[0] - numbers[1]
		if operator == '*':
			return numbers[0] * numbers[1]
		if operator == '/':
			return numbers[0] / numbers[1]
	except ArithmeticError:
		return None
	raise ValueError('Invalid operator! op: {0}'.format(operator))


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
	values = list(numbers)
	affected_indexes = []
	for p in priority:
		curr_numbers = values[p], values[p + 1]
		curr_operator = operators[p]
		curr_value = calculate_single_op(curr_numbers, curr_operator)
		if curr_value is None:
			return None
		values[p], values[p + 1] = curr_value, curr_value

		if p in affected_indexes or p + 1 in affected_indexes:
			for i in affected_indexes:
				values[i] = curr_value

		elif len(affected_indexes) != 0:
			affected_indexes = range(4)

		affected_indexes += [i for i in (p, p + 1) if i not in affected_indexes]

	if int(values[0]) != values[0]:
		return None
	
	return int(values[0])


def get_all_values(numbers, operators_list, priorities):
	"""
	Finds all the different values that we can find by applying the each of the operators
	sets given to us in any possible order to the numbers rearranged in any possible order.
	Note that this function only returns unique elements, and remove all that are below 1 / None.
	:param numbers: a list containing 4 integers.
	:param operators_list: a list containing lists of 3 chars representing arithmetic operators.
	:param priorities: a list of the different priorities that dictate the order in which we'll
	use the operators on the numbers.
	:return: a list as described above, without any repeating values, without None and without
	0.
	"""
	numbers_list = get_singular_show_sets([], numbers)
	values = []
	for n in numbers_list:
		for priority in priorities:
			for operators in operators_list:
				values.append(calculate_value(n, priority, operators))

	return extract_interesting_list(values)


def extract_interesting_list(values_list):
	"""
	returns a list containing a singular show of each element in values_list.
	Removes each item that is smaller than 1 (or None). Also sorts the list.
	"""
	values_list = list(set(values_list))
	values_list = [val for val in values_list if val is not None and val > 0]
	temp = list(values_list)
	values_list.sort()
	return values_list


def get_amount_of_consecutive_numbers(vals_list):
	"""
	Returns the amount of consecutive numbers from 1.
	:param vals_list: a list of all the numbers achieved using calculate_value on a given
	list of numbers with all possible operators and in all the possible orders.
	:return: an integer.
	"""
	count = 0
	if vals_list[0] != 1:
		return count

	for i in xrange(len(vals_list) - 1):
		count += 1
		if vals_list[i] != vals_list[i + 1] - 1:
			break

	return count


def get_all_numbers():
	"""
	:return: a list containing all possible tuples of a,b,c,d when all of those are single digits
	and a<b<c<d.
	"""
	numbers = []
	for a in xrange(1, 7):
		for b in xrange(a + 1, 8):
			for c in xrange(b + 1, 9):
				for d in xrange(c + 1, 10):
					numbers.append([float(d) for d in (a, b, c, d)])
					# numbers.append((a, b, c, d))

	return numbers


def find_longest_consecutive_set():
	"""
	Finds the 4 numbers a<b<c<d that form a list containing the longest chain of consecutive
	integers when we perform every possible set of operators on them in all possible orders.
	:return:
	"""
	longest_consecutive = 0
	longest_set = None
	numbers_list = get_all_numbers()
	priorities = get_singular_show_sets([], range(3))
	ops = get_repeating_show_sets([], OPS, 3)
	bar = ProgressBar()
	for numbers in bar(numbers_list):
		vals = get_all_values(numbers, ops, priorities)
		length = get_amount_of_consecutive_numbers(vals)
		if length > longest_consecutive:
			longest_consecutive = length
			longest_set = numbers

	return longest_set, longest_consecutive


def test():
	ops = get_repeating_show_sets([], OPS, 3)
	numbers = get_singular_show_sets([], [1, 2, 3, 4])
	priorities = get_singular_show_sets([], range(3))
	vals = get_all_values([1.0, 2.0, 3.0, 4.0], ops, priorities)
	print len(vals)
	print vals
	print get_amount_of_consecutive_numbers(vals)


def main():
	longest_set, length = find_longest_consecutive_set()
	print "The set that yields the longest consecutive possible numbers from 1 to n is :{0}, n: {1}".format(longest_set, length)


main()
