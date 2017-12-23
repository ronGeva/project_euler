def binary_search(sorted_list, value):
	"""
	Searches value in the sorted list using binary search.
	Returns the index of value. If not found returns -1.
	"""
	floor_index = 0
	roof_index = len(sorted_list) 
	while floor_index < roof_index - 1:
		mid_index = (floor_index + roof_index) / 2
		if sorted_list[mid_index] < value:
			floor_index = mid_index 
		elif sorted_list[mid_index] > value:
			roof_index = mid_index
		else:
			return mid_index
	
	if sorted_list[0] == value:
		return 0
	return -1


def main():
	"""
	Tests will be run in main.
	"""
	pass

if __name__ == '__main__':
	main()
