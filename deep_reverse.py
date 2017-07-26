def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for l in L:
        print("[", end=" ")
        for i in range(1,len(l)+1):
            print(l[-i], end=" " )
        print("]")

deep_reverse([[1, 2], [3, 4], [5, 6, 7]])
