from ex73 import is_proper_fraction

def find_biggest_fraction(n_limit):
	biggest_fraction = -1
	result = (-1, -1)
	for d in xrange(8, n_limit + 1):
		ratio = d / 7.0
		n = int(ratio * 3)
		while not is_proper_fraction(n, d):
			n -= 1
		if biggest_fraction < n / float(d):
			biggest_fraction = n / float(d)
			result = (n, d)
	return result

def main():
	print "searching the biggest proper fraction that is smaller than 3/7, where d <= 1,000,000..."
	print "result is : {0}".format(find_biggest_fraction(1000000))

if __name__ == '__main__':
	main()