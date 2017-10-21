import math

MINIMUM_PANDIGITAL = 123456789
NUMBER_STR = "123456789"
MAX_NUM_TO_CHECK = 9999

def update_pandigital(num, new_num):
	return num * pow(10, math.ceil(math.log10(new_num))) + new_num

def create_pandigital(num):
	i = 2
	pandigital = num
	next_pan = pandigital
	while pandigital < MINIMUM_PANDIGITAL:
		new_num = num * i
		pandigital = update_pandigital(pandigital, new_num)
		i += 1
	return pandigital

def is_pandigital(num):
	if math.floor(math.log10(num)) != 8:
		return False

	digits_list = list(str(int(num)))
	digits_list.sort()
	digits_str = "".join(digits_list)
	return digits_str == NUMBER_STR

def find_biggest_pandigital():
	biggest_pan = MINIMUM_PANDIGITAL
	for i in xrange(1, MAX_NUM_TO_CHECK + 1):
		pandigital = create_pandigital(i)
		if is_pandigital(pandigital) and pandigital > biggest_pan:
			biggest_pan = pandigital

	return biggest_pan

def main():
	print "Beginning searching for the biggest pandigital number!"
	biggest_pan = find_biggest_pandigital()
	print "The biggest pandigital number is {0}".format(biggest_pan)

if __name__ == '__main__':
	main()

