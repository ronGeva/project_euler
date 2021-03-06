import math
from pe_useful import is_prime, binary_search

#SUBSET_SIZE = 5
SUBSET_SIZE = 4

min_sum = 99999999999
min_five = []


def get_all_primes(limit):
	primes = []
	for num in xrange(2, limit):
		if is_prime(num):
			primes.append(num)
	return primes

def get_all_subsets(numbers, set_size):
	subsets = []
	if set_size == 1:
		subsets = [[num] for num in numbers]
	else:
		num = numbers[0]
		new_numbers = list(numbers)
		new_numbers.remove(num)
		subsets = [[num] + subset for subset in get_all_subsets(new_numbers, set_size - 1)]
		if set_size <= len(new_numbers):
			subsets += get_all_subsets(new_numbers, set_size)

	return subsets


def is_prime_pair(prime1, prime2, all_primes):
	possible_prime_1 = int(str(prime1) + str(prime2))
	possible_prime_2 = int(str(prime2) + str(prime1))
	return binary_search(all_primes, possible_prime_1) != -1 and binary_search(all_primes, possible_prime_2) != -1


def get_plpl(limit):
	primes = get_all_primes(limit)
	from math import log
	all_primes = get_all_primes(pow(limit, 2))
	plpl_dict = {}
	for prime1 in primes:
		for prime2 in primes:
			if is_prime_pair(prime1, prime2, all_primes):
				if prime1 in plpl_dict.keys():
					plpl_dict[prime1].append(prime2)
				else:
					plpl_dict[prime1] = [prime2]
	return plpl_dict

def is_five_tuple_good(numbers, plpl_dict):
	for num in numbers:
		new_numbers = list(numbers)
		new_numbers.remove(num)
		for num2 in new_numbers:
			if not num2 in plpl_dict[num]:
				return False
	return True

def check_if_five(prime, plpl_dict):
	global min_sum
	global min_five
	candidates = plpl_dict[prime]
	if len(candidates) < SUBSET_SIZE - 1:
		return
	subsets = get_all_subsets(candidates, SUBSET_SIZE - 1)
	subsets = [[prime] + subset for subset in subsets]
	for subset in subsets:
		if is_five_tuple_good(subset, plpl_dict):
			curr_sum = sum(subset)
			if curr_sum < min_sum:
				min_sum = curr_sum
				min_five = subset

def find_smallest_sum(limit):
	plpl_dict = get_plpl(limit)
	for prime in plpl_dict.keys():
		check_if_five(prime, plpl_dict)

def main():
	limit = int(raw_input("Enter limit==>"))
	find_smallest_sum(limit)
	print "Smallest sum : {0}, min five : {1}".format(min_sum, min_five)

if __name__ == '__main__':
	main()