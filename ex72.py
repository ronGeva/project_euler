import time

def get_all_prime_dividers(n):
	i = 2
	prime_dividers = [1]
	while n > 1:
		if n % i == 0:
			prime_dividers.append(i)
			n /= i
		else:
			i += 1
	return prime_dividers

def get_prime_dividers_list(max_num):
	prime_div_l = []
	for num in xrange(2, max_num + 1):
		prime_div_l.append(get_all_prime_dividers(num))
	return prime_div_l

def main():
	start_time = time.time()
	l = get_prime_dividers_list(20000)
	print "finished in {0} sec".format(time.time() - start_time)

if __name__ == '__main__':
	main()