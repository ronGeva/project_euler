import random

ONE_THIRD = 1 / 3.0
HALF = 1 / 2.0

def in_range(n, d):
	value = n / float(d)
	return value < HALF and value > ONE_THIRD

def get_gcd(n, d):
	dividened = d
	divisor = n
	remainder = dividened % divisor
	while remainder != 0:
		dividened = divisor
		divisor = remainder
		remainder = dividened % divisor
	return divisor

def is_proper_fraction(n, d):
	return get_gcd(n, d) == 1

def count_proper_fractions(limit):
	count = 0
	for d in xrange(3, limit + 1):
		for n in xrange(int(d / 3.0 + 1), int(d / 2.0) + 1):
			if is_proper_fraction(n, d):
				count += 1
	return count

def test_gcd_func():
	for i in xrange(10):
		n = int(random.uniform(1, 200))
		d = int(random.uniform(1, 200))
		print "n: {0}, d : {1} , gcd : {2}".format(min(n, d), max(n, d), get_gcd(min(n, d), max(n, d)))

if __name__ == '__main__':
	proper_fractions = count_proper_fractions(12000)
	print "amount of proper_fractions between 1/2 and 1/3, represented as n/d when d <= 12K is\
	{0}".format(proper_fractions)
