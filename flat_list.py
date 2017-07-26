def flatten(aList):
    """ 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    """
    if isinstance(aList, list):

        if len(aList) == 0:
            return []
       
        f,l= aList[0],aList[1:]
        return flatten(f) + flatten(l)
    

    else:
        return[aList]


print(flatten([[1]]))
print(flatten([1,2,3,6]))
print(flatten([[[2]]]))
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
