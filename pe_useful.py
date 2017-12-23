import math, time, random, os, json

def is_prime(num):
	maximum_divider = int(math.sqrt(math.fabs(num))) + 1
	for i in xrange(2, maximum_divider):
		if num % i == 0:
			return False
	return True

def binary_search(sorted_list, num):
	#returns the index of num in sorted_list. If not found, returns -1.	
	roof_index = len(sorted_list)
	floor_index = -1
	while(roof_index > floor_index + 1):
		mid_index = (roof_index + floor_index) / 2
		if sorted_list[mid_index] == num:
			return mid_index
		if sorted_list[mid_index] > num:
			roof_index = mid_index
		else:
			floor_index = mid_index
	return -1

def fill_digit_dict(num, digit_dict):
	"""
	sets digit dict to contain the following data:
	digit_dict[digit_key] = the amount of times this digit appears
	in num.
	digit dict must contain a key for each possible digit beforehand.
	returns None.
	"""
	while num > 0:
		try:
			digit_dict[num % 10] += 1
		except:
			print digit_dict, num
		num /= 10

def is_permutation(num1, num2):
	"""
	:param num1: integer.
	:param num2: integer.
	returns True if num1 is a permutation of num2.
	Complexity: 
	"""
	digit_dict1, digit_dict2 = {}, {}
	for i in xrange(10):
		digit_dict1[i], digit_dict2[i] = 0, 0
	
	fill_digit_dict(num1, digit_dict1)
	fill_digit_dict(num2, digit_dict2)

	return digit_dict1 == digit_dict2

def get_all_primes(limit):
	"""
	all_numbers -> a boolean list, if True then the number is composite,
	otherwise it is false.

	Complexity: O(n)
	"""
	primes = [1]
	all_numbers = []
	for i in xrange(limit):
		all_numbers.append(False)

	for index in xrange(2, limit):
		#if number is composite, move on
		if all_numbers[index]:
			continue

		#the current index is a prime. since it isn't composite.
		primes.append(index)
		multiplier = 2
		while index * multiplier < limit:
			all_numbers[index * multiplier] = True
			multiplier += 1

	return primes

def get_all_prime_dividers(num, primes):
	"""
	returns all the prime dividors of num, provided a list of all primes
	up to num.
	Complexity: O(sqrt(num) * log(sqrt(num)))
	"""
	prime_dividers = []
	possible_divider = 2
	while possible_divider <= int(math.sqrt(num)) and num > 1:
		#if i isn't a prime, continue to the next number
		if binary_search(primes, possible_divider) != -1:
			if num % possible_divider == 0:
				prime_dividers.append(possible_divider)
			while(num % possible_divider == 0):
				num /= possible_divider

		possible_divider += 1

	if num != 1:
		prime_dividers.append(num)

	return prime_dividers

def phi(n, prime_dividers):
	"""
	returns phi(n) using euler's totient function and its prime dividers.
	Complexity: O(1)~ = O(len(prime_dividers))
	"""
	num_of_strange_numbers = n
	for prime_divider in prime_dividers:
		num_of_strange_numbers *= (1 - 1.0 / prime_divider)

	return int(round(num_of_strange_numbers))

def save_progress(args, process_name):
	directory = os.getcwd()
	new_dir = os.path.join(directory, "progressVars_" + process_name) 
	if not os.path.isdir(new_dir):
		os.mkdir(new_dir)

	for i in xrange(len(args)):
		file_path = os.path.join(new_dir, "arg " + str(i))
		with open(file_path, 'w') as f:
			f.write(json.dumps(args[i]))

def load_progress(process_name):
	args = []
	our_directory = os.path.join(os.getcwd(), "progressVars_" + process_name)
	try:
		args_path = os.listdir(our_directory)
	except WindowsError:
		return args
	for arg_path in args_path:
		full_path = os.path.join(our_directory, arg_path)
		with open(full_path, 'r') as f:
			args.append(json.load(f))

	return args

def get_all_squares(limit):
	"""
	:param limit: an integer representing the highest number to have its
	square in the returned list.
	returns a list of all squares from 0 to limit.
	"""
	return [pow(num, 2) for num in xrange(limit + 1)]

def test_func(func):
	def new_func():
		starting_time = time.time()
		func()
		print "time passed: {0} seconds".format(time.time() - starting_time)
	return new_func

@test_func
def test_binary_search():
	l = [1,2,3,5,7,11,13]
	print binary_search(l, 20)

@test_func
def test_get_all_primes():
	l = get_all_primes(10000000)

@test_func
def test_phi():
	primes = get_all_primes(100)
	num = 210
	prime_dividers = get_all_prime_dividers(num, primes)
	phi_n = phi(num, prime_dividers)
	print "phi({0}) : {1}".format(num, phi_n)

def test_save_and_load():
	l = [1,2,3,4,5]
	d = {'a': 1, 'b': 3}
	x = 5
	save_progress([l, d, x], 'test')
	print load_progress('test')

if __name__ == '__main__':
	test_phi()
