import math

def is_prime(num):
	maximum_divider = int(math.sqrt(math.fabs(num))) + 1
	for i in xrange(2, maximum_divider):
		if num % i == 0:
			return False
	return True
