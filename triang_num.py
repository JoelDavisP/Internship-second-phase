def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    if k==0:
        return False
    if k==1:
        return True
    else:
        sums = 1
        for i in range(2,k):
            sums = sums+i
            if sums==k:
                return True
                break
            
        return False

print(is_triangular(3))
print(is_triangular(6))
print(is_triangular(5))
print(is_triangular(8))

