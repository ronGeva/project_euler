from pe_useful import is_permutation

def is_permu_for_multiplication(num, multiplication):
	return is_permutation(num, num * multiplication)

def find_permu_for_all_multi(multi_limit):
	"""
	Finds a num who is a permutation of himself when multiplied
	by all numbers from 2 to multi_limit.
	:param multi_limit: integer.
	returns integer.
	"""
	num = 2
	continue_searching = True
	while continue_searching:
		num += 1
		continue_searching = False
		for multiplier in xrange(2, multi_limit + 1):
			if not is_permu_for_multiplication(num, multiplier):
				continue_searching = True
				break
	return num

def main():
	print find_permu_for_all_multi(6)

if __name__ == '__main__':
	main()
	