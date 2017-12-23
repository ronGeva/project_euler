from math import ceil
import progressbar

def count_all_sets(n, set_size, max_size):
	if n == set_size:
		return 1

	initial_num = min(n - set_size + 1, max_size)
	total_sets = 0
	for num in xrange(initial_num, int(ceil(n / float(set_size))) - 1, -1):
		total_sets += count_all_sets(n - num, set_size - 1, num)

	return total_sets

def get_amount_of_combinations(num, show_bar=False):
	num_of_combs = 0
	if show_bar:
		bar = progressbar.ProgressBar()
		for set_size in bar(xrange(1, num + 1)):
			num_of_combs += count_all_sets(num, set_size, num)

	else:
		for set_size in xrange(1, num + 1):
			num_of_combs += count_all_sets(num, set_size, num)		

	return num_of_combs

def main():
	num = int(raw_input("Find number of possible combination for number==>"))
	num_of_combs = get_amount_of_combinations(num, True)

	print "num of possible combinations is ", num_of_combs

if __name__ == '__main__':
	main()