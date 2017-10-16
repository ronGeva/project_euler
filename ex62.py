LIMIT_NUM = 10000

def get_key(num):
	key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	while num > 0:
		curr_digit = num % 10
		key[curr_digit] += 1
		num /= 10

	key = [str(digit_count) for digit_count in key]
	key = "".join(key)

	return key

def ex62():
	permut_dict = {}
	canidate_list = []
	for num in xrange(1, LIMIT_NUM):
		cubic_val = pow(num, 3)
		key = get_key(cubic_val)
		if key in permut_dict.keys():
			permut_dict[key][0] += 1
			if permut_dict[key][0] == 5:
				canidate_list.append(permut_dict[key][1])
			elif permut_dict[key][0] == 6:
				canidate_list.remove(permut_dict[key][1])
		else:
			permut_dict[key] = [1, cubic_val]
	return canidate_list[0]

def main():
	result = ex62()
	print "smallest cube who has exactly 4 other cubic permutations is {0}".format(result)

if __name__ == '__main__':
	main()