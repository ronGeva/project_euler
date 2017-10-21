import math

def get_triangle_num(curr_index):
	if curr_index % 2 == 0:
		return (curr_index + 1) * (curr_index / 2)

	else:
		return (curr_index + 1) * (curr_index / 2) + (curr_index / 2 + 1)

def is_prime(num):
	largest_factor = int(math.sqrt(num)) + 1
	for i in xrange(2, largest_factor):
		if num % i == 0:
			return False

	return True

def get_prime_factors(num):
	prime_dividors = []
	curr_divider = 2
	while num > 1:
		if not is_prime(curr_divider):
			curr_divider += 1
			continue

		while num % curr_divider == 0:
			prime_dividors.append(curr_divider)
			num /= curr_divider

		curr_divider += 1

	return prime_dividors

def get_num_of_factors(prime_dividors):
	prime_dividors.sort()
	num_of_factors = 1
	index = 0
	while index < len(prime_dividors):
		curr_prime = prime_dividors[index]
		power = prime_dividors.count(curr_prime) 
		num_of_factors *= (power + 1)
		while index < len(prime_dividors) and curr_prime == prime_dividors[index]:
			index += 1

	return num_of_factors

def main():
	index = 2
	num_of_factors = 2
	while num_of_factors <= 500:
		index += 1
		triangle_num = get_triangle_num(index)
		prime_dividors = get_prime_factors(triangle_num)
		num_of_factors = get_num_of_factors(prime_dividors)
	
	print "The triangle num is {0}".format(triangle_num)

if __name__ == '__main__':
	main()