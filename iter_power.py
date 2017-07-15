def iterPower(base, exp):
	if exp==0:
		return 1
	elif exp==1:
		return base	
	else:
		i = exp
		val = base
		while i != 1:
			val = val * base
			i -= 1    
		return val

print(iterPower(4,5))
