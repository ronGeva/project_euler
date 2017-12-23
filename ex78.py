from ex76 import get_amount_of_combinations

def find_amound_divisible_by_n(n):
	num = 2
	curr_amount = 2
	while (curr_amount % n != 0):
		num += 1
		curr_amount = get_amount_of_combinations(num)

	return num, curr_amount

def main():
	n = int(raw_input("Enter number you'd like your amount of combinations to be divided by==>"))
	result = find_amound_divisible_by_n(n)
	print "you can divide {0} in {1} ways, meaning it's divisible by {1}".format(result[0], result[1], n)

if __name__ == '__main__':
	main()