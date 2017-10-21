import math

def get_all_int_triangles(num_ceiling):
	int_triangles = []
	for a in xrange(1, num_ceiling):
		for b in xrange(1, num_ceiling):
			c = math.sqrt(pow(a, 2) + pow(b, 2))
			if c.is_integer():
				int_triangles.append((a, b, c))
	return int_triangles

def count_matches(p, int_triangles):
	count = 0
	for triangle in int_triangles:
		if sum(triangle) == p:
			count += 1
	return count

def find_maximised_p(int_triangles):
	most_matches = 0
	best_p = 0
	for p in xrange(3, 1001):
		matches = count_matches(p, int_triangles)
		if matches > most_matches:
			most_matches = matches
			best_p = p
	return best_p

def main():
	int_triangles = get_all_int_triangles(1000)
	print find_maximised_p(int_triangles)

if __name__ == '__main__':
	main()