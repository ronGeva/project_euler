EXPRESSIONS = [(0.5, 0.5), (1, 0), (1.5, -0.5), (2, -1), (2.5, -1.5), (3, -2)]

def get_all_figurates(floor_limit, ceiling_limit, expression):
	"""
	returns all figurate numbers that are created using the expression
	provided and are within the range provided.
	:param floor_limit: a value all figurate numbers returned must be larger
	than.
	:param ceiling_limit: a value all figurate numbers returned must be smaller
	than.
	:param expression: a tuple representing the expression in the following 
	convention: (amount of n^2, amount of n).
	for example: get_all_figurates(10, 20, (1, 1/2)) will return - 
	[10, 18] -> [3 ^ 2 + 3 / 2, 4 ^ 2 + 4 / 2]
	"""
	triangles = []
	n = 1
	continue_flag = True
	while continue_flag:
		new_triangle = expression[0] * pow(n, 2) + expression[1] * n
		if floor_limit < new_triangle < ceiling_limit:
			triangles.append(new_triangle)

		elif new_triangle > ceiling_limit:
			continue_flag = False

		n += 1

	return triangles

def test():
	for expression in EXPRESSIONS:
		print get_all_figurates(0, 100, expression)

if __name__ == '__main__':
	test()