from pe_useful import is_permutation, phi
import progressbar


def generate_dividing_primes_list(maximal_number):
	"""
	Returns a list representing the dividing primes for each number.
	The index of each cell in the list represent the number itself while its value is the list of primes which divide
	it.
	:param maximal_number: The maximal number to look for, or the size of the returned list minus 1 (since the number 0
	will technically be included in the list).
	:return: The generated dividing primes list.
	"""
	print "Generating an empty list of {amount} cells...".format(amount=maximal_number + 1)
	dividing_primes = [[] for num in xrange(maximal_number + 1)]

	print "Generating dividing primes list..."
	for num in progressbar.progressbar(xrange(2, maximal_number + 1)):
		if len(dividing_primes[num]) == 0:  # congratz, you're a prime
			for curr_num in xrange(num, len(dividing_primes), num):
				dividing_primes[curr_num].append(num)
	return dividing_primes


def main():
	dividing_primes_list = generate_dividing_primes_list(pow(10, 7))
	phi_minimum = (1, 0)  # This is the biggest minimum
	print "Checking phi value and is permutation for each number..."
	for num in progressbar.progressbar(xrange(2, len(dividing_primes_list))):
		phi_value = phi(num, dividing_primes_list[num])
		# num/phi_value < best_num/best_phi -> num * best_phi < best_num * phi_value
		if num * phi_minimum[1] < phi_minimum[0] * phi_value and is_permutation(phi_value, num):
			phi_minimum = (num, phi_value)

	print "Minimal ratio goes to number {num}, with phi value: {phi}".format(num=phi_minimum[0], phi=phi_minimum[1])
	print phi_minimum


main()