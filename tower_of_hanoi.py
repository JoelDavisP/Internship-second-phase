def mov(fr,to):
	print("Ring is moving from " + str(fr) + " to "+ str(to))
def tow_of_han(n,front,to,spare):
	"""
	input: An instance of Tower of Hanoi problem, that contains 4
	       parameters, first one is the total number of rings, second
		   one is from which tower it is moving, third one to which
		   tower it is moving and the last one is the spare tower
	output: The movements that solve tower of Hanoi
	"""
	if n == 1:
		mov(front,to)
	else:
		tow_of_han(n-1,front,spare,to)
		tow_of_han(1,front,to,spare)
		tow_of_han(n-1,spare,to,front)

print(tow_of_han(4,'T1','T2','T3'))
