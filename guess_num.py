def fn(low,high):
	""" 
	input: two integers first the lower bound and then upper bound
	Returns an integer in between this bound which you guessed
	"""
 	mid = (low+high)//2
	print("Is your secret number: ",mid)
	inp = raw_input("\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly\n")
	
	if(inp == 'h'):
		high = mid
		fn(low,high)
	elif(inp == 'l'):
		low = mid
		fn(low,high)
	elif(inp == 'c'):
		print("This is the number in your mind", mid)
			#break
	else:
		print("Sorry I cant recogonize you")
		fn(low,high)
low = 0
high = 100
mid = (low + high)//2
print("\nWelcome to the guessing game!!")
print("\nPlease think of a number between 0 and 100")
fn(low,high)
