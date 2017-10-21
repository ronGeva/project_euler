def check_if_valid_text(text):
	e_count = text.count('e')
	space_count = text.count(" ")
	if '}' in text or '{' in text:
		return False
	return e_count > 10 and space_count > 10

def decrypt(key, cipher):
	plain = ""
	for i in xrange(len(cipher)):
		char_val = key[i % len(key)] ^ cipher[i]
		
#		if char_val < 65 or char_val > 127:
#			return ""
		
		plain += chr(char_val)
	if not check_if_valid_text(plain):
		return ""

	return plain

def find_key(cipher):
	count = 0
	for key_1 in xrange(97, 123):
		for key_2 in xrange(97, 123):
			for key_3 in xrange(97, 123):
				key = (key_1, key_2, key_3)
				plain = decrypt(key, cipher)
				count += 1
				if plain != "":
					print "key : {0}, plain = {1}".format(key, plain)

def get_sum(cipher, key):
	plain = decrypt(key, cipher)
	return sum([ord(char) for char in plain])


def main():
	input_data = open('ex59_input.txt', 'rb').read().replace("\n", "")
	numbers_str = input_data.split(",")
	numbers = [int(number) for number in numbers_str]
	print get_sum(numbers, (103, 111, 100))

if __name__ == '__main__':
	main()