def palin(s):
	"""" 
	input: a string to check whether it is a palindrome or not
	output: True if it is a palindrome, else false
	"""
	def tochar(s):
		""" 
		input: a string of any type of charecters in any case
		Result: a string that only contains small letter alphabets
		"""
		s= s.lower()
		a = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				a += c
		return a
	def check(s):
		"""
		recursive checking function of palindrome
		"""
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and check(s[1:-1])
	return check(tochar(s))


print(palin("Abba, I'm mia.;:'bba"))	
print(palin("ydyjxutf"))
