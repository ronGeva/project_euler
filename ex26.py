from decimal import Decimal
from math import floor

BIG_NUM = 9999999999999999999999.0

def is_int(num):
	return floor(num) == num

def main():
	for d in xrange(3, 100):
		if is_int(BIG_NUM / d):
			print d

if __name__ == '__main__':
	main()

