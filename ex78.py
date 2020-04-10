"""
let's define number of possible partition for number of coins n is p(n)
p(n) = sum((-1)^(k-1) * p(n-gk)) where
gk = k(3k-1)/2 for k in series -> (1, -1, 2, -2, 3...)
"""
import time

from pe_useful import test_func
from progressbar import ProgressBar

PRINT_INTERVAL = 10 # in seconds

class PartitionCalculator(object):
	def __init__(self):
		self.summation_counts = {}

	def get_k(self, index):
		return pow(-1, index) * ((index + 2) / 2)

	def get_gk(self, index):
		k = self.get_k(index)
		return k * (3 * k - 1) / 2, k

	def count_summations(self, num):
		if num in self.summation_counts.keys():
			return self.summation_counts[num]

		if num <= 1:
			return 1

		count = 0
		index = 0
		gk, k = self.get_gk(index)
		while gk <= num:
			count += (int(pow(-1, k - 1)) * self.count_summations(num - gk))
			index += 1
			gk, k = self.get_gk(index)

		self.summation_counts[num] = count
		return count

	def find_least_divisible(self, dividor):
		"""
		returns the least number that has a total ways of being represented by the sum of integers divisible
		by the dividor argument.
		"""
		pc = PartitionCalculator()
		num = 1
		last_print_time = time.time()
		while True:
			count = pc.count_summations(num)
			if time.time() - last_print_time > PRINT_INTERVAL:
				print "num {0}, count {1}".format(num, count)
				last_print_time = time.time()
			if count % dividor == 0:
				break
			num += 1
		print "num {0} is the least number divisible by {1}, count is {2}!!!".format(num, dividor, count)
					

def main():
	pc = PartitionCalculator()
	pc.find_least_divisible(1000000)

def test():
	n = int(raw_input("Enter number you'd like your amount of combinations to be divided by==>"))
	pc = PartitionCalculator()
	for n in xrange(1, 100):
		print str(n), str(pc.count_summations(n))

if __name__ == '__main__':
	main()