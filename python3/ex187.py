"""
Find the amount of positive numbers below 10^8 which has exactly two (not necessarily distinct) prime factors.

Algorithm:
1. Find all the primes up to (10^8)/2, keep the primes in a sorted list.
2. For each prime x find all primes y such that
2-1. x < y
2-2  x * y < 10^8
3. Step #2 can be performed using a binary search on the list obtained in step #1.
"""


from primes import get_all_primes


LIMIT = pow(10, 8)


def biggest_compatible_prime_index(sorted_primes: list[int], prime_index: int, limit: int) -> int:
	"""
	Find the index of the biggest prime p such that (sorted_primes[prime_index], p) is a compatible tuple.
	Complexity: O(log(n))
	"""
	p = sorted_primes[prime_index]
	top = len(sorted_primes)
	bottom = -1
	while top > bottom + 1:
		mid = (top + bottom) // 2
		if sorted_primes[mid] * p > limit:
			top = mid
		else:
			bottom = mid

	# Make sure we get the index of the biggest
	last_compatible_index = min(bottom, top)
	while sorted_primes[last_compatible_index] * p < limit:
		last_compatible_index += 1
	last_compatible_index -= 1

	return last_compatible_index


def count_compatible_primes(sorted_primes: list[int], prime_index: int, limit: int) -> int:
	"""
	Count how many primes in sorted_primes are compatible with sorted_primes[prime_index].
	An ordered tuple (p1, p2) is considered compatible iif:
	- p1*p2 < limit
	- p1 <= p2
	:param sorted_primes: A list of all primes up to limit.
	:param prime_index: The index of the prime whose amount of compatible tuples we'd like to find.
	:param limit: The used for the definition of a compatible prime tuple.
	:return: The amount of ordered tuples (p1, p2) which are compatible and for which p1 == sorted_primes[prime_index].
	Complexity: O(log(n))
	"""
	last_compatible_index = biggest_compatible_prime_index(sorted_primes, prime_index, limit)

	# +1 because the prime factors don't have to be distinct
	compatible_primes_amount = max(last_compatible_index - prime_index + 1, 0)
	return compatible_primes_amount


def solution():
	primes = get_all_primes(LIMIT, with_one=False)
	count = 0
	for prime_index in range(len(primes)):
		count += count_compatible_primes(primes, prime_index, LIMIT)
	print(count)


if __name__ == '__main__':
	solution()
