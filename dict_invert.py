def dict_invert(d):
    """
    d: dict
    Returns an inverted dictionary when you input a dictionary.
    The inverse of a dictionary d is another dictionary whose keys are the 
    unique dictionary values in d. 
    The value for a key in the inverse dictionary is a sorted list 
    (increasing order) of all keys in d that have the same value in d. 
    """
    dic_inv = {}
    for i in d:
        if dic_inv=={} or d[i] not in dic_inv.keys():
            dic_inv[d[i]]=[i]
        #elif d[i] not in dic_inv.keys():
         #   dic_inv[d[i]] = [i]
        else:
            dic_inv[d[i]].append(i)
    
    for i in dic_inv:
        dic_inv[i].sort()

    return dic_inv



dict_invert({5:10, 6:20, 1:10,8:20,9:30,2:20, 3:30, 4:30})
        
