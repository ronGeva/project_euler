def count_distinct_powers(a_max, b_max):
	distinct_powers = []
	for a in xrange(2, a_max + 1):
		for b in xrange(2, b_max + 1):
			num = pow(a, b)
			if num not in distinct_powers:
				distinct_powers.append(num)

	return len(distinct_powers)

def main():
	print "calculating number of premutations of a**b when 2<=a<=100 and 2<=b<=100"
	print "count = {0}".format(count_distinct_powers(100, 100))

if __name__ == '__main__':
	main()