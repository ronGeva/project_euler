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

def is_condition_met(digit, t, numbers_priority):
	index = t.index(digit)
	prev_digit = get_previous(t, index)
	next_digit = get_next(t, index)
	prev_flag, next_flag = True, True
	

def guess_shortest_code(tries, numbers_priority):
	for t in tries:
		for index in xrange(3):
			digit = t[index]
			next_digit = get_next(t, index)
			prev_digit = get_previous(t, index)

			if not next_digit is None and next_digit in numbers_priority:
				if digit in numbers_priority:
					numbers_priority.remove(digit)
				next_digit_index = numbers_priority.index(next_digit)
				numbers_priority.insert(next_digit_index, digit)

			elif not prev_digit is None and prev_digit in numbers_priority:
				if digit in numbers_priority:
					numbers_priority.remove(digit)
				prev_digit_index = numbers_priority.index(prev_digit)
				numbers_priority.insert(prev_digit_index + 1, digit)

	return numbers_priority

def test():
	tries = get_tries()
	numbers_priority = []
	set_starting_vars(tries, numbers_priority)
	for i in xrange(10):
		numbers_priority = guess_shortest_code(tries, numbers_priority)
	print numbers_priority

if __name__ == '__main__':
	test()