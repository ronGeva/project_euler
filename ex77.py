from pe_useful import get_all_primes
from progressbar import ProgressBar

class StrKeyedDict(object):
	def __init__(self):
		self.inner_dict = {}
	def __getitem__(self, key):
		return self.inner_dict[str(key)]
	def __setitem__(self, key, val):
		self.inner_dict[str(key)] = val
	def has_key(self, key):
		return str(key) in self.inner_dict.keys()

def count_prime_summations(num, primes, curr_summation, all_summations):
	if num < 2:
		if num == 0 and not all_summations.has_key(curr_summation):
			all_summations[curr_summation] = True
			return 1
		return 0
	count = 0
	for prime in primes:
		if num - prime >= 0:
			if len(curr_summation) == 0 or prime >= curr_summation[-1]:
				count += count_prime_summations(num - prime, primes, curr_summation + [prime], all_summations)
		else:
			break
	return count


def ex77(number_limit):
	primes = get_all_primes(number_limit, with_one=False)
	d = StrKeyedDict()
	bar = ProgressBar()
	for num in bar(xrange(2, number_limit)):
		prime_summations = count_prime_summations(num, primes, [], d)
		if prime_summations >= 5000:
			print "The number {0} has {1} prime summations".format(num, prime_summations)
			break

def main():
	limit = 300
	ex77(limit)

if __name__ == '__main__':
	main()