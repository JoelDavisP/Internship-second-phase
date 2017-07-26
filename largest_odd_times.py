def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None 
    """
    cnt = {}
    oddnum=[]
    for i in set(L):
        cnt[i] = L.count(i)
    for i,count in cnt.items():
        if count%2 != 0:
            oddnum.append(i)
    if len(oddnum) == 0:
        return
    else:
        return max(oddnum)     



print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,5,7,11,11,11,11,11,7,7,7,7,3,5,3]))
