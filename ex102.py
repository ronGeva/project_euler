"""
Count how many triangles contain the point (0,0) inside of them, given 1000 triangles.

Given a triangle T with points P1, P2, P3, it is safe to assume that if we create a new triangle T' using 2 of these
points (we'll assume these are P1 and P2 for simplicity) and replacing the third with (0,0) we'll get a triangle in
 which the angle between P1 and (0,0) and the angle between P2 and (0,0) both are smaller than the angles between
 P1 to P3 and P2 to P3 respectively.
We can verify this using trigo:
Angle of P1: arccos( ((P1P2)^2 + (P1P3)^2 - (P2P3)^2)/(2*(P1P2)*(P1P3)) ), in other words:
angle of A: arcos ( (b^2 + c^2 - a^2) / 2bc )
"""
from math import sqrt, fabs, acos
from os.path import dirname, abspath, join


def calc_distance(p1, p2):
	"""
	Calcualte the distnace between 2 points (each points is a 2 tuple).
	"""
	return sqrt(pow(fabs(p1[0] - p2[0]), 2) + pow(fabs(p1[1] - p2[1]), 2))


def calc_angle(a, b, c):
	"""
	Calculate a single angle.
	:param a: The side in front of the angle being calculated.
	:param b: One of the side forming the angle.
	:param c: The other side forming the angle.
	:return: The angle (in radians).
	"""
	return acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))


def calc_angles(points):
	"""
	Calculate the angles of the triangle, given its sides. For the following triangle: (P1, P2, P3), returns
	the following angles: (angle of P1, angle of P2, angle of P3).
	:param points: An iterable containing 3 points, each represented using a 2 tuple (indicating its location in the 2
	dimensional space).
	:return: (angle of P1, angle of P2, angle of P3) in radians.
	"""
	distances = [calc_distance(p1, p2) for p1, p2 in ((points[0], points[1]), (points[0], points[2]),
													  (points[1], points[2]))]  # order by P1-P2, P1-P3, P2-P3
	angles = []
	for angle_index in range(3):
		a = distances[2 - angle_index]  # for P1 a is P2P3, for P2 a is P1P3, for P3 a is P1P2
		b, c = set(distances) - {a}
		angles.append(calc_angle(a, b, c))

	return angles


def verify_triangle(triangle):
	"""
	Returns True if (0,0) is contained within the triangle, otherwise - False.
	"""
	angles = calc_angles(triangle)
	for i in xrange(3):
		new_triangle = list(triangle)
		new_triangle.pop(i)  # pop the i-th point
		prev_angles = list(angles)
		prev_angles.pop(i)

		new_triangle.insert(i, (0, 0))
		new_angles = calc_angles(new_triangle)
		new_angles.pop(i)  # we don't care about the angle in (0, 0), it can be (and it should) be bigger than the others

		if any([prev_angles[j] <= new_angles[j] for j in xrange(2)]):
			return False
	return True


def main():
	"""
	Iterate through the input file's triangles, and calculate how many of them contain (0,0).
	:return:
	"""
	input_path = join(dirname(abspath(__file__)), 'ex102_input.txt')
	with open(input_path, 'r') as f:
		lines = f.read().splitlines()
	triangles = []
	for line in lines:
		numbers = [int(num) for num in line.split(",")]
		triangle = []
		for i in range(3):
			triangle.append((numbers[i * 2], numbers[i * 2 + 1]))
		triangles.append(triangle)
	count = 0
	for triangle in triangles:
		if verify_triangle(triangle):
			count += 1
	print count


if __name__ == '__main__':
	main()
