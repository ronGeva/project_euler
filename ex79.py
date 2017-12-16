def get_tries():
	data = None
	with open('ex79_input.txt', 'r') as f:
		data = f.read()

	tries = data.split("\n")
	tries.remove('')
	return tries

def get_next(t, index):
	if index == 2:
		return None
	return t[index + 1]

def get_previous(t, index):
	if index == 0:
		return None
	return t[index - 1]

def set_starting_vars(tries, numbers_priority):
	for digit in tries[0]:
		numbers_priority.append(digit)

	tries.pop(0)


def is_correctly_relative(digit, other_digit, numbers_priority, next):
	"""
	next : True for next digit, False for previous digit
	"""
	if other_digit is None or not other_digit in numbers_priority:
		return True

	digit_index = numbers_priority.index(digit)
	if(next):
		for i in xrange(digit_index, len(numbers_priority)):
			if numbers_priority[i] == other_digit:
				return True
	else:
		for i in xrange(digit_index, -1, -1):
			if numbers_priority[i] == other_digit:
				return True

	return False

def is_condition_met(digit, t, numbers_priority):
	index = t.index(digit)
	prev_digit = get_previous(t, index)
	next_digit = get_next(t, index)

	return is_correctly_relative(digit, next_digit, numbers_priority, True) and \
	is_correctly_relative(digit, prev_digit, numbers_priority, False)

def fix_location(digit, t, numbers_priority):
	if digit in numbers_priority:
		if is_condition_met(digit, t, numbers_priority):
			return
		numbers_priority.remove(digit)
	for index in xrange(0, len(numbers_priority)):
		numbers_priority.insert(index, digit)
		if is_condition_met(digit, t, numbers_priority):
			return
		numbers_priority.remove(digit)
	

def guess_shortest_code(tries, numbers_priority):
	for t in tries:
		for index in xrange(3):
			digit = t[index]
			fix_location(digit, t, numbers_priority)
	return numbers_priority

def test():
	tries = get_tries()
	numbers_priority = []
	set_starting_vars(tries, numbers_priority)
	for i in xrange(3):
		numbers_priority = guess_shortest_code(tries, numbers_priority)
	print numbers_priority

if __name__ == '__main__':
	test()