"""
Non-bouncy numbers

A non-bouncy number is a number whose digits appear in incrementing/decrementing order throughout the entirety of the
number.
For example: 1122334 is non-bouncy and 13522 is bouncy (since 1 < 3 < 5 > 2...).
We want to find the number of bouncy numbers below a threshold.

Solution:
A number of (k+1) digits that is non-bouncy is one of the following:
0 followed by any k-digits number that is incrementing, or a k-digits numbers which is decrementing and starting with 0.
1 followed by any k-digits number that starts with the digits 1/2/.../9 and is incrementing, or with 1/0 and is
decrementing.
...
9 followed by an incrementing k-digits number starting with 9 or a decrementing 9-digits number starting with 9/8/...1.

Therefore, if we compute for every k digits the amount of incrementing and decrementing numbers starting with 0 to 9
(for each category) we can compute these values for (k+1) digits in O(1).
"""
# counter[k][n] represents the amount of incrementing/decrementing numbers with k digits starting with the digit n
Counter = dict[int, dict[int, int]]


def initialize_counters(max_digits: int) -> tuple[Counter, Counter]:
	incrementing_numbers = {k: {} for k in range(1, max_digits)}
	decrementing_numbers = {k: {} for k in range(1, max_digits)}
	for num in range(0, 10):
		incrementing_numbers[1][num] = 1
		decrementing_numbers[1][num] = 1
	return incrementing_numbers, decrementing_numbers


def compute_incrementing_and_decrementing_numbers(max_digits: int, incrementing_numbers: Counter,
												  decrementing_numbers: Counter) -> None:
	for k in range(2, max_digits):
		for num in range(0, 10):
			incrementing_possibilities = 0
			for next_digit in range(num, 10):
				incrementing_possibilities += incrementing_numbers[k - 1][next_digit]
			incrementing_numbers[k][num] = incrementing_possibilities

			decrementing_possibilities = 0
			for next_digit in range(num, -1, -1):
				decrementing_possibilities += decrementing_numbers[k - 1][next_digit]
			decrementing_numbers[k][num] = decrementing_possibilities


def count_total_non_bouncy_numbers(max_digits: int, incrementing_numbers: Counter,
												  decrementing_numbers: Counter) -> int:
	total_incrementing_numbers = 0
	total_decrementing_numbers = 0
	for k in range(max_digits - 1, 0, -1):
		for starting_digit in range(1, 10):
			total_incrementing_numbers += incrementing_numbers[k][starting_digit]
			total_decrementing_numbers += decrementing_numbers[k][starting_digit]

	same_digit_numbers = (max_digits - 1) * 9

	return total_incrementing_numbers + total_decrementing_numbers - same_digit_numbers


def solution(max_digits):
	incrementing_numbers, decrementing_numbers = initialize_counters(max_digits)
	compute_incrementing_and_decrementing_numbers(max_digits, incrementing_numbers, decrementing_numbers)
	return count_total_non_bouncy_numbers(max_digits, incrementing_numbers, decrementing_numbers)


def main():
	print("Amount of non-bouncy numbers below 10^100 is {}".format(solution(101)))


if __name__ == '__main__':
	main()
