"""
A number with n digits is in the range 10^(n-1) => 10^n - 1.
We can represent this number as y^n (y is a natural num).
Therefore: 10^(n-1) <= y^n <= 10^n -1.
We can conclude that y must be smaller than 10 (since 10^n > 10^n -1).
Finally, all we need to make sure is that the other condition is met:
y^n >= 10^(n-1).
"""

def get_range(y):
	count = 0
	n = 1
	while(pow(y, n) >= pow(10, n - 1)): #second condition
		count += 1
		n += 1
	return count

def ex63():
	count = 0
	for y in xrange(1, 10): #first condition
		count += get_range(y)
	return count

def main():
	result = ex63()
	print "the total number of n-digit positive integers which are also an nth power is {0}".format(result)

if __name__ == '__main__':
	main()