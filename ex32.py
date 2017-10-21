import string
DIGITS = string.digits[1:]

def check_if_pandigital(multipicand, multiplier, product):
	st = str(multipicand) + str(multiplier) + str(product)
	l = [letter for letter in st]
	l.sort()
	st = "".join(l)

	return st == DIGITS

def is_valid(multipicand, multiplier, products, product):
	overall_len = len(str(multipicand) + str(multiplier) + str(product))

	return overall_len == 9 and product not in products

def calc_sum(num_ceiling):
	products = []
	for multipicand in xrange(2, num_ceiling + 1):
		for multiplier in xrange(2, num_ceiling + 1):
			product = multipicand * multiplier
			if is_valid(multipicand, multiplier, products, product):
				if check_if_pandigital(multipicand, multiplier, product):
					products.append(product)

	return sum(products), products

def main():
	print "calculating the sum of all 9 digits pandigital products:"
	print "sum, products are = {0}".format(calc_sum(9000))

if __name__ == '__main__':
	main()