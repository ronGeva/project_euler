def solution(upper_limit: int):
	"""
	For each number n (1 < n < M) we can find all the numbers in the range [1, M] that are divided by it simply
	by multiplying n by every positive number until we've exceeded the upper limit M.
	The amount of time required to find all the number dividable by 2 is M/2, for 3 it is M/3 and so on and so forth.
	Overall, this functions runs in sum(M/k) for k: 2->M, which means it takes O(M * log(M)).
	"""
	divisors = [0 for _ in range(upper_limit)]
	for num in range(2, upper_limit):
		divided_by_num = num * 2
		while divided_by_num < upper_limit:
			divisors[divided_by_num] += 1
			divided_by_num += num

	return sum([1 if divisors[n] == divisors[n + 1] else 0 for n in range(2, upper_limit - 1)])


def main():
	print("Number of integers 1 < n < 10^7 for which the amount of positive divisors of n and n+1 is identical is "
		  "{}".format(solution(pow(10, 7))))


if __name__ == '__main__':
	main()
