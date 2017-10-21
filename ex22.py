def get_name_value(name, index):
	value = 0
	for letter in name:
		value += ord(letter) - 64

	return value * index

def get_values_list(names):
	values_l = []
	for index in xrange(len(names)):
		values_l.append(get_name_value(names[index], index + 1))

	return values_l

def main():
	input_data = open('ex22_input.txt', 'rb').read()
	input_data = input_data.replace('"', '')
	names = input_data.split(",")
	names.sort()

	values_l = get_values_list(names)
	print "The sum of all the names' values is {0}".format(sum(values_l))

if __name__ == '__main__':
	main()