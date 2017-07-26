def print_without_vowels(s):
    """
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    """
    l= ['a','e','i','o','u','A','E','I','O','U']
    new=[]
    for i in s:
        if i not in l:
            new.append(i)
    newstr=''.join(new)
    return newstr

print(print_without_vowels("This is great!"))

print(print_without_vowels("Thvhdayib lmhg8yojsdiydgcdushn!"))
print(print_without_vowels("This is greacucigvct!"))
print(print_without_vowels("This is grftfcyMPJmeat!"))
print(print_without_vowels("This is grAAHFJVOeioopuioeoPMPKnjeat!"))
