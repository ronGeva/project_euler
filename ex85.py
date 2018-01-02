import progressbar

def count_amount_of_rectangle(height, width):
	"""
	All possible inner rectangles inside a rectangle with known height 
	and width are the sum of height terms of a fixed formula
	that behaves like an Arithmetic Progression times the same formula 
	using the width paremeter instead.
	"""
	return ((1 + height) * height / 2) * ((1 + width) * width / 2)

def check_if_new_smallest(smallest_fit, rectangle_amount_floor_limit, curr_amount):
	return rectangle_amount_floor_limit < curr_amount and curr_amount < smallest_fit

def find_smallest_rectangle(rectangle_amount_floor_limit, sides_max):
	smallest_fit = pow(rectangle_amount_floor_limit, 2) #something big
	chosen_rectangle = (-1, -1)
	bar = progressbar.ProgressBar()
	for height in bar(xrange(1, sides_max)):
		width_roof = sides_max + 1
		width_floor = -1
		best_width = None
		while width_roof > width_floor + 1:
			mid_width = (width_floor + width_roof) / 2
			curr_amount = count_amount_of_rectangle(height, mid_width)
			if curr_amount > rectangle_amount_floor_limit:
				if count_amount_of_rectangle(height, mid_width - 1) < rectangle_amount_floor_limit:
					best_width = mid_width
					break
				width_roof  = mid_width
			else:
				if count_amount_of_rectangle(height, mid_width + 1) > rectangle_amount_floor_limit:
					best_width = mid_width + 1
					break
				width_floor = mid_width

		if not best_width is None:
			curr_amount = count_amount_of_rectangle(height, best_width)
			if check_if_new_smallest(smallest_fit, rectangle_amount_floor_limit, curr_amount):
				smallest_fit = curr_amount
				chosen_rectangle = (height, best_width)

	print "smallest amount of rectangle that is still bigger than {0} is\
	{1}".format(rectangle_amount_floor_limit, smallest_fit)

	difference = abs(rectangle_amount_floor_limit - smallest_fit)
	return chosen_rectangle, difference

def main():
	"""
	Right now only finds the smallest amount that is bigger than rectangle_amount_floor_limit
	provided. In order to be hermetic double check is needed, once using 2M in order to find
	smallest difference above 2M, than using the same function on 2M - the difference found.

	"""
	first_rect, first_diff = find_smallest_rectangle(2000000, 50000)
	second_rect, second_diff = find_smallest_rectangle(2000000 - first_diff, 50000)
	print "The grid that produces the closest result to 2 million is:"
	if first_diff > second_diff:
		print second_rect

	else:
		print first_rect


if __name__ == '__main__':
	main()