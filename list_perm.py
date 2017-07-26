def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
    """ 
    cnt1={}
    cnt2={}
    if len(L1) == 0 and len(L2) == 0:
        return (None,None,None)
    if len(L1) == len(L2):
        for i in set(L1):
            cnt1[i] = L1.count(i)
        for j in set(L2):
            cnt2[j] = L2.count(j) 
        if cnt1 == cnt2:
            for x,cnt in cnt1.items():
                if cnt == max(cnt1.values()):
                    return(x,cnt,type(x))
        else:
            return False

    else:
        return False   


L1 = ['a', 'a', 'b'] 
L2 = ['a', 'b']
L3 = [1, 'b', 1, 'c', 'c', 1] 
L4 = ['c', 1, 'b', 1, 1, 'c']




print(is_list_permutation(L1,L2))
print(is_list_permutation(L3,L4))
print(is_list_permutation([], []))
