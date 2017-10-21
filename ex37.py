import math

def is_prime(num):
	largest_factor = int(math.sqrt(num)) + 1
	for i in xrange(2, largest_factor):
		if num % i == 0:
			return False

	return True

def is_truncatable_prime(num):
	temp = num
	while temp > 0:
		if not is_prime(temp):
			return False
		temp /= 10

	temp = str(num)
	index = 1
	while index < len(temp):
		if not is_prime(int(temp[index:])):
			return False
		index += 1

	return True
	

def find_truncatable_primes(amount_of_primes):
	truncatable_primes = []
	num = 11
	while len(truncatable_primes) < amount_of_primes:
		if is_truncatable_prime(num):
			truncatable_primes.append(num)
		num += 2

	return truncatable_primes

def main():
	print sum(find_truncatable_primes(11))


if __name__ == '__main__':
	main()