"""
Bouncy numbers
"""


def is_bouncy(num):
	digits_list = [digit for digit in str(num)]
	is_increasing = (sorted(digits_list) == digits_list)
	is_decreasing = (sorted(digits_list, reverse=True) == digits_list)
	return not is_increasing and not is_decreasing


def get_proportions(current_num, found_bouncy):
	return (found_bouncy / float(current_num)) * 100


def find_least_index_for_proportion(wanted_proportion):
	current_num = 101  # first possibly bouncy number according to problem's description
	found_bouncy = 0
	if is_bouncy(current_num):
		found_bouncy += 1
	while get_proportions(current_num, found_bouncy) != wanted_proportion:
		current_num += 1
		if is_bouncy(current_num):
			found_bouncy += 1
	return current_num


def main():
	print find_least_index_for_proportion(99)


main()