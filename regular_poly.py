import math
def polysum(n,s):
	"""
	input: Two arguments 'n' and 's'. 'n' stands for number of sides and 's'	       stands for each side length (regular polygon have same length for 		   all sides)
	output: sum of the area and square of the perimeter of the regular 
	        polygon. Function returns the sum, rounded to 4 decimal places.

	"""
	pi = math.pi
	area = (0.25*n*s**2)/math.tan(pi/n)
	perim = n*s
	print(type(area))
	print(type(perim))
	return float("%.4f" %(area + (perim**2)))

print(polysum(4,6))
print(polysum(3,3))
print(polysum(5,7))
