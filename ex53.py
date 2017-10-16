N_LIMIT = 100
MILLION = 1000000

def azeret(num):
	result = 1
	while num > 1:
		result *= num
		num -= 1
	return result

def combinatoric_selections(n, r):
	return azeret(n) / (azeret(r) * azeret(n - r))

def ex53():
	count = 0
	for n in xrange(1, N_LIMIT + 1):
		for r in xrange(1, n + 1):
			if combinatoric_selections(n, r) > MILLION:
				count += 1
	return count

def main():
	print "There are {0} values of nCr (1<n<100) that are greater than million".format(ex53())
if __name__ == '__main__':
	main()