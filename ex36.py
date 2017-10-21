def is_pelindrome(num_st):
	mid_index = len(num_st) / 2
	for i in xrange(mid_index):
		if num_st[i] != num_st[-i - 1]:
			return False

	return True

def find_all_double_base_pelindromes(num_ceiling):
	double_base_pelindromes = []
	for i in xrange(1, num_ceiling):
		dec_str = str(i)
		bin_str = str(bin(i))[2:]
		if is_pelindrome(dec_str) and is_pelindrome(bin_str):
			double_base_pelindromes.append(i)

	return double_base_pelindromes

def main():
	print sum(find_all_double_base_pelindromes(1000000))

if __name__ == '__main__':
	main()