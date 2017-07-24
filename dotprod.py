def dotProduct(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    """
    sum_list = 0
    x = []
    for l in range(len(listA)):
        x.append(listA[l]*listB[l])
    for i in x:
        sum_list += i

    return sum_list

A=[1,2,3]
B=[4,5,6]

print(dotProduct(A,B))
