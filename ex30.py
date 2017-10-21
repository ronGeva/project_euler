
def is_digits_fifth_power(num):
	temp = num
	digits_sum = 0
	while num > 0:
		digit = num % 10
		num /= 10
		
		digits_sum += pow(digit, 5)

	return digits_sum == temp

def calc_sum(num_ceiling):
	numbers = []
	num_sum = 0
	for num in xrange(2, num_ceiling + 1):
		if is_digits_fifth_power(num):
			num_sum += num
			numbers.append(num)

	return num_sum, numbers


def main():
	print "calculating the sum of all the numbers that are equal to the"
	print "sum of the fifth power of their digits:"
	print "Num sum = {0}".format(calc_sum(355000))
	

if __name__ == '__main__':
	main()