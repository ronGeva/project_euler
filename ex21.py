from ex12 import get_prime_factors

def get_all_factors(num):
	factors = []
	for i in xrange(1, num):
		if num % i == 0:
			factors.append(i)

	return factors

def get_all_amicable_numbers(max_num):
	fact_sum_to_num = {}
	amicable_nums = []

	for i in xrange(1, max_num):
		factors_sum = sum(get_all_factors(i))
		if i in fact_sum_to_num.keys() and factors_sum == fact_sum_to_num[i]:
			amicable_nums.append(i)
			amicable_nums.append(fact_sum_to_num[i])
		else:
			fact_sum_to_num[factors_sum] = i

	return amicable_nums

def main():
	print sum(get_all_amicable_numbers(10000))

if __name__ == '__main__':
	main()