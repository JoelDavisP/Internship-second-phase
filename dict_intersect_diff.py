def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    """
    inter={}
    diff={}
    l1=d1.keys()
    l2=d2.keys()
    for l in l1:
        if l in l2:
            inter[l]=f(d1[l],d2[l])
    for l in l1:
        if l not in l2:
            diff[l] = d1[l]
    for x in l2:
        if x not in l1:
            diff[x] = d2[x]
    return (inter,diff)

def f(x,y):
    return x+y


print(dict_interdiff({1:30, 2:20, 3:30,9:40,11:71, 5:80},{1:40, 2:50, 3:60, 4:70, 6:90}))
