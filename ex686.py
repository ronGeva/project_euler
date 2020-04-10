"""
Basis for this solution:
log(x*y) = log(x) + log(y)
log(x^y) = y*log(x)

We're looking for j that answers the condition:
123 * 10^x <= 2^j < 124 * 10^x -> log(123*10^x, 2) <= j < log(124*10^x,2) ->
log(123, 2) + log(10^x, 2) <= j and j < log(124) + log(10^x,2) ->
log(123, 2) + x*log(10, 2) <= j and j < log(124) + x*log(10,2) ->
log(123, 2) <= j - x * log(10, 2) < log(124)

"""
from sys import argv
from math import log


LOG_10 = log(10, 2)


def check(bottom, upper, j, l_multiplier):
	return bottom <= j - l_multiplier < upper


def get_valid_x(upper, current_l_multipler, j):
	while upper + current_l_multipler < j:
		current_l_multipler += LOG_10
	return current_l_multipler


def find_nth_power(L, n):
	current_l_multipler = 0
	j = 0
	found_powers = 0
	bottom = log(L, 2)
	upper = log(L + 1, 2)
	while found_powers < n:
		current_l_multipler = get_valid_x(upper, current_l_multipler, j)
		if check(bottom, upper, j, current_l_multipler):
			found_powers += 1
		j += 1
	return j - 1


def main(args):
	L = int(args[1])
	n = int(args[2])
	print find_nth_power(L, n)


main(argv)