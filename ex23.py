
def get_all_proper_divisors(num):
	proper_divisors = []
	for possible_dividor in xrange(1, num / 2 + 1):
		if num % possible_dividor == 0:
			proper_divisors.append(possible_dividor)
	return proper_divisors

def is_abundant(num):
	return sum(get_all_proper_divisors(num)) > num

def get_all_abundant_numbers(limit):
	abundant_numbers = []
	for num in xrange(limit + 1):
		if is_abundant(num):
			abundant_numbers.append(num)
	return abundant_numbers

def get_bool_filled_list(size_of_list):
	"""
	Creates a list in which each element will represent whether or
	not the number at its index is the sum of two abundant numbers.
	"""
	new_list = []
	for i in xrange(size_of_list):
		new_list.append(False)
	return new_list

def find_all_sums_of_abundants(empty_list, abundant_numbers):
	for abundant1 in abundant_numbers:
		for abundant2 in abundant_numbers:
			empty_list[abundant1 + abundant2] = True

def find_sum_of_all_false(bool_list):
	result = 0
	for num in xrange(28213):
		if not bool_list[num]:
			result += num

	return result

def main():
	abundant_numbers = get_all_abundant_numbers(28213)
	print abundant_numbers[:10]
	bool_list = get_bool_filled_list(28213 * 2)
	find_all_sums_of_abundants(bool_list, abundant_numbers)
	print find_sum_of_all_false(bool_list)

if __name__ == '__main__':
	main()