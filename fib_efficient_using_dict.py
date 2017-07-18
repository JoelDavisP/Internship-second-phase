def fib_effic(n):
	"""
	input: a number 'n' to which the fibonacci number is to be			 printed
	output: fibonacci number of 'n'
	"""
	d = {1:0, 2:1}
	if n in d:
		return d[n]
	else:
		ans = fib_effic(n-1) + fib_effic(n-2)
		d[n] = ans
		return d[n]

#print(fib_effic(6))
print(fib_effic(1))
print(fib_effic(15))
print(fib_effic(9))
print(fib_effic(7))
