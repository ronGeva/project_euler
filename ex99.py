from pe_useful import get_gcd
from random import randint
from math import log10
from progressbar import ProgressBar


def get_exponents():
	data_lines = None
	with open('ex99_input.txt', 'rb') as f:
		data_lines = f.readlines()
	return [[int(num) for num in line.split(",")] for line in data_lines]


def is_bigger(exp1, exp2):
	"""
	By logarithms rules, log(a^b) = b * log(a).
	Log(a^b) ? Log(c^d) doesn't change the status between those two values (The bigger one will remain bigger).
	:param exp1: a list containing base and exponent.
	:param exp2: a list containing base and exponent.
	:return: The value of exp1 > exp2.
	"""
	log_exp1_val = exp1[1] * log10(exp1[0])
	log_exp2_val = exp2[1] * log10(exp2[0])
	return log_exp1_val > log_exp2_val


def naive_is_bigger(exp1, exp2):
	return pow(exp1[0], exp1[1]) > pow(exp2[0], exp2[1])

def test():
	for i in xrange(8000):
		a = randint(1, 100)
		b = randint(1, 100)
		c = randint(1, 100)
		d = randint(1, 100)
		naive_result = naive_is_bigger([a, b], [c, d])
		my_result = is_bigger([a, b], [c, d])
		if naive_result != my_result:
			print a, b, c, d, "Not good!", naive_result, my_result


def main():
	bar = ProgressBar()
	exps = get_exponents()
	biggest_exp = exps[0]
	for exp in bar(exps[1:]):
		if is_bigger(exp, biggest_exp):
			biggest_exp = exp

	print "Biggest exponent is {0}".format(biggest_exp)
	print "Its line number is {0}".format(exps.index(biggest_exp))


if __name__ == '__main__':
	main()
