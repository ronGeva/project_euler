from pe_useful import is_prime

def f(n, a, b):
	return pow(n, 2) + a * n + b

def count_consecutive_primes(a, b):
	n = 0
	while(is_prime(f(n, a, b))):
		n += 1
	return n

def get_all_primes(min_val, max_val):
	primes = []
	for num in xrange(min_val, max_val + 1):
		if is_prime(num):
			primes.append(num)
	return primes

def find_most_consecutive_primes(min_val, max_val):
	primes = get_all_primes(min_val, max_val)
	best_vars = (0, 0)
	most_consecutive = 0
	for a in xrange(min_val, max_val):
		for b in primes:
			curr_consecutive = count_consecutive_primes(a, b)
			if curr_consecutive > most_consecutive:
				most_consecutive = curr_consecutive
				best_vars = (a, b)
	return best_vars

def main():
	a, b = find_most_consecutive_primes(-1000, 1000)
	print "a: {0}, b: {1}, a * b = {2}".format(a, b, a * b)

if __name__ == '__main__':
	main()
