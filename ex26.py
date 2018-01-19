from progressbar import ProgressBar

AMOUNT_OF_DIGITS = 10000
MINIMUM_SIZE_CYCLE = 1
MAXIMUM_SIZE_CYCLE = 2500


def is_repeating(st, remaining_st):
	length = len(st)
	index = 0
	while index + length < len(remaining_st):
		if st != remaining_st[index:index + length]:
			return False
		index += length

	return True

def find_recurring_cycle(num):
	cycle = str(pow(10, AMOUNT_OF_DIGITS) / num)
	s_index = 0
	for s_index in xrange(AMOUNT_OF_DIGITS / 4):
		curr_cycle = cycle[s_index:MINIMUM_SIZE_CYCLE]
		for curr_cycle_size in xrange(MINIMUM_SIZE_CYCLE, MAXIMUM_SIZE_CYCLE - s_index):
			if is_repeating(cycle[s_index:curr_cycle_size + s_index], cycle[curr_cycle_size + s_index:]):
				return curr_cycle_size
	return -1

def find_longest_cycle(limit):
	biggest_cycle = 0
	best_num = -1
	bar = ProgressBar()
	for num in bar(xrange(2, limit)):
		curr_cycle = find_recurring_cycle(num)
		if curr_cycle > biggest_cycle:
			biggest_cycle = curr_cycle
			best_num = num

	return best_num, biggest_cycle

def main():
	num, biggest_cycle = find_longest_cycle(1000)
	print """The number yielding the longest recurring cycle in
	its decimal fraction part is :"""
	print "{0} ! And the cycle's length is {1}".format(num, biggest_cycle)

if __name__ == '__main__':
	main()
