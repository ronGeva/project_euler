def get_all_primes(limit: int, with_one: bool=True) -> list[int]:
	"""
	all_numbers -> a boolean list, if True then the number is composite,
	otherwise it is false.

	Complexity: O(n)
	"""
	if with_one:
		primes = [1]
	else:
		primes = []
	all_numbers = []
	for i in range(limit):
		all_numbers.append(False)

	for index in range(2, limit):
		# if number is composite, move on
		if all_numbers[index]:
			continue

		# the current index is a prime. since it isn't composite.
		primes.append(index)
		multiplier = 2
		while index * multiplier < limit:
			all_numbers[index * multiplier] = True
			multiplier += 1

	return primes
