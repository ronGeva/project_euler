import time
import progressbar
import os
import signal
import sys

from math import sqrt
from pe_useful import binary_search, phi, get_all_primes, get_all_prime_dividers,\
 test_func, save_progress, load_progress


def fill_digit_dict(num, digit_dict):
	while num > 0:
		try:
			digit_dict[num % 10] += 1
		except:
			print digit_dict, num
		num /= 10

def is_permutation(num1, num2):
	digit_dict1, digit_dict2 = {}, {}
	for i in xrange(10):
		digit_dict1[i], digit_dict2[i] = 0, 0
	
	fill_digit_dict(num1, digit_dict1)
	fill_digit_dict(num2, digit_dict2)

	return digit_dict1 == digit_dict2

def get_vars(limit):
	args = load_progress('ex70')
	if len(args) == 0:
		return [999, 2, get_all_primes(limit)]

	else:
		return args

def find_max_totient_permutation(limit):
	min_ratio, min_ratio_num, primes = get_vars(limit)

	def close_program(signal, frame):
		args = [min_ratio, min_ratio_num, primes]
		save_progress(args, 'ex70')
		sys.exit(0)

	signal.signal(signal.SIGINT, close_program)

	bar = progressbar.ProgressBar()
	for num in bar(xrange(min_ratio_num, limit)):
		prime_dividers = get_all_prime_dividers(num, primes)
		phi_n = phi(num, prime_dividers)
		if is_permutation(num, phi_n) and num / float(phi_n) < min_ratio:
			min_ratio = num / float(phi_n)
			min_ratio_num = num

	return min_ratio_num


def main():
	start_time = time.time()
	print "searching for the max num/phi(num) where phi(num) is a permutation of num..."
	print "Found it! num = {0}".format(find_max_totient_permutation(10000000))
	print "time passed : {0} seconds".format(time.time() - start_time)

def test():
	print is_permutation(87109, 79180)
	print is_permutation(1132, 2311)
	print is_permutation(10101, 10100)

if __name__ == '__main__':
	main()