import math

LIMIT_NUM = 100000

def is_prime(num):
	biggest_divider = int(math.sqrt(num)) + 1
	for i in xrange(2, biggest_divider):
		if num % i == 0:
			return False
	return True

def get_permut_num(num, digit_to_change):
	count = 0
	for possible_value in xrange(0, 10):
		permut = int(str(num).replace(digit_to_change, str(possible_value)))
		if is_prime(permut):
			count += 1
	return count

def ex51():
	for i in xrange(2, LIMIT_NUM):
		pass

def main():
	print get_permut_num(13, '1')

if __name__ == '__main__':
	main()