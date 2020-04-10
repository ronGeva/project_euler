"""

"""

def find_b(t):
	"""
	Given t => total amount of discs, returns the total amount of blue
	discs so that the chances of drawing 2 blue discs one after another
	is 50%.
	"""
	a, b, c = 2 , -2, t - pow(t, 2)
	return (-b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)


