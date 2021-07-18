"""
Diagonal of a Cube

Create a function that takes the volume of a cube and returns the length of the cube's main diagonal, rounded to two decimal places.

Examples
cube_diagonal(8) ➞ 3.46

cube_diagonal(343) ➞ 12.12

cube_diagonal(1157.625) ➞ 18.19

Notes
Use the sqrt function in the math module.
"""



################################################################
"""
Solution 1
"""


import math

def cube_diagonal(volume):
	return round(math.sqrt(3) * pow(volume, 1/3), 2)



################################################################
"""
Solution 2
"""


def cube_diagonal(volume):
	def find_sides(volume):
		return volume ** (1/3)
	def find_diag(a, b):
		return (((a ** 2) + (b ** 2)) + (a ** 2)) ** .5
	
	sides = find_sides(volume)
	
	return round(find_diag(sides, sides), 2)



################################################################
"""
Solution 3
"""


cube_diagonal = lambda v: round(__import__("math").sqrt(3 * v ** (2 / 3)), 2)


