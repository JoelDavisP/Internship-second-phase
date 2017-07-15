def count_vowel(s):
	ls = ['a', 'e', 'i', 'o', 'u','A', 'E','I','O', 'U']
	count = 0
	for letter in s:
		if letter in ls:
			count += 1
	print "Number of Vowels:", count
count_vowel('azcbobobegghakl')
