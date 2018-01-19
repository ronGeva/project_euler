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
			triangles.append(int(new_triangle))

		elif new_triangle > ceiling_limit:
			continue_flag = False

		n += 1

	return triangles

def is_cyclic(num1, num2):
	return num1 % 100 == num2 / 100

def extract_list(container_list):
	if type(container_list[0][0]) == list:
		return extract_list([item[0] for item in container_list])

	return container_list

def find_full_cycle(curr_cycle, available_lists):
	"""
	Finds all full cycles for the incomplete cycle provided.
	If no cycle is found, returns None
	"""
	if len(available_lists) == 0:
		return curr_cycle

	last_num = curr_cycle[-1]
	found_cycles = []
	for available_list in available_lists:
		for possible_num in available_list:
			if is_cyclic(last_num, possible_num):
				found_cycle = find_full_cycle(curr_cycle + [possible_num], 
					[l for l in available_lists if l != available_list])

				if not found_cycle is None:
					found_cycles.append(found_cycle)
	if len(found_cycles) == 0:
		return None

	return found_cycles

def is_list_cyclic(possible_cyclic_list):
	"""
	returns true if the last item is cyclic to the first item.
	"""
	return is_cyclic(possible_cyclic_list[-1], possible_cyclic_list[0])

def find_figurate_cycle(figurate_lists):
	starting_list = figurate_lists[0]
	figurate_lists.pop(0)
	found_cycles = []
	for num in starting_list:
		new_found_cycles = find_full_cycle([num], figurate_lists)
		if not new_found_cycles is None:
			found_cycles.append(new_found_cycles)

	found_cycles = extract_list(found_cycles)
	#found_cycles = filter(is_list_cyclic, found_cycles)

	return found_cycles

def test():
	figurate_lists = [get_all_figurates(999, 10000, expression) for expression in EXPRESSIONS[:6]]
	print find_figurate_cycle(figurate_lists)

if __name__ == '__main__':
	test()