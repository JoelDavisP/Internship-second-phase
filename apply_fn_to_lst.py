def apply_to_each(L,F):
	"""
	Input is a list of elements, named \"L\" and a function \"F\".
	Output: A new list returned after applying the following changes
			to every elements in the list, i.e. element e in the older
			list will become f(e).
	"""
	for i in range(len(L)):
		L[i] = F(L[i]) 
	return L


L = [1,-2,-9.6,5,7.8,3.5,-22,98,244,-4.0]
print(L)
print(apply_to_each(L,abs))
print(apply_to_each(L,int))
print(apply_to_each(L,fact))
print(apply_to_each(L,fib))
