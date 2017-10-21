def factorial(num):
	factorial = 1
	for i in xrange(2, num + 1):
		factorial *= i

	return factorial

def get_digits_factorials(num):
	factorials = []
	while num > 0:
		digit = num % 10
#		if digit == 0:
#			num /= 10
#			continue

		factorials.append(factorial(digit))
		num /= 10

	return factorials

def find_digit_factorials(num_ceiling):
	digit_factorials = []
	for num in xrange(10, num_ceiling + 1):
		factorials = get_digits_factorials(num)
		if sum(factorials) == num:
			digit_factorials.append(num)

	return digit_factorials

def main():
	digit_factorials = find_digit_factorials(2000000)
	print digit_factorials
	print sum(digit_factorials)

if __name__ == '__main__':
	main()