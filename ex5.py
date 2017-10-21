PRINT_DATA = """Enter max number, the program will calculate
the smallest number that is evenly divided in all
the numbers up to your input number==>"""

def is_removeable(mul_sum, curr_num, max_num):
	mul_sum_after_divide = mul_sum / curr_num
	for num in xrange(2, max_num + 1):
		if mul_sum_after_divide % num != 0:
			return False

	return True

def lower_number_as_possible(mul_sum, max_num):
	for num in xrange(2, max_num + 1):
		if is_removeable(mul_sum, num, max_num):
			mul_sum /= num

	return mul_sum


def calc_smallest_mul(max_num):
	mul_sum = 1
	for num in xrange(2, max_num + 1):
		if mul_sum % num != 0:
			mul_sum *= num

	mul_sum = lower_number_as_possible(mul_sum, max_num)
	return mul_sum

def main():
	max_num = int(raw_input(PRINT_DATA))
	print "The number is {0}".format(calc_smallest_mul(max_num))

if __name__ == '__main__':
	main()