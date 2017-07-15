
"""
    input:  input a positive integer
    prints the closest cube root of that number

"""

x=int(input("Enter value\n"))
eps = 0.01
num_guess = 0
low = 1
high = x
guess = (low + high)/2.0
while abs(guess**3 - x) >= eps:
	if guess**3 < x:
		low = guess
	else:
		high = guess
	guess = (low + high)/2.0
	num_guess += 1
print('  number of guesses = ', num_guess)
print(guess, '  is close to the cube root of', x )
