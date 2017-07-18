def how_many(aDict):
	"""
	Input: A dictionary, contain lists as values.
	Output: Returns the key with the largest number of values associated
		    with it
	"""
	res = None
	big = 0
	for key in aDict.keys():
		if len(aDict[key]) >= big:
			res = key
			big = len(aDict[key])
	return res
dic = {'b': [1,2], 'd': [3,6,64], 'a': [7,1], 'c': [3]}
print(how_many(dic))
