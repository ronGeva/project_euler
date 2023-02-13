def is_reversible(num: int):
	if (num % 10) == 0:
		return False

	reversed_num = int(str(num)[::-1])
	num_sum = num + reversed_num
	while num_sum > 0:
		if num_sum % 2 == 0:
			return False
		num_sum //= 10
	return True


def main():
	count = 0
	for i in range(1000, 10000):
		if is_reversible(i):
			print(i)
			count += 1
	print(count)


if __name__ == '__main__':
	main()
