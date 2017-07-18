def how_many(aDict):
	"""
	Input: A dictionary, contain lists as values.
	Output: Returns a number which is the total values of that dictionary
	"""
	count = 0
	b = []
	b = aDict.values()
	c = []
	for i in range(len(aDict)):
		c.append(len(b[i]))
	count = list_sum(c)
	return count
def list_sum(lists):
	"""
	Input: A list of numbers
	Output: A number that is the sum of all elements of that list
	"""
	sum_list = 0
	for i in range(len(lists)):
		sum_list += lists[i]
	return sum_list


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['d'].append('dog')
animals['c'].append('cat')
animals['a'].append('aana')
animals['c'].append('cricket')
animals['d'].append('dinosar')
animals['b'].append('black sheep')
animals['b'].append('buffallo')
animals['a'].append('ace')
animals['a'].append('apple')
animals['c'].append('cockroach')
print(animals)
print(how_many(animals))
