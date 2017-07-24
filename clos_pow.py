def closest_power(base, num):
    """
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    """
    dic={}
    if num == 1:
        return 0
    else:
        a = 1
        dif = []
        while base**a < num:
            a+=1
        dic[abs(num-base**a)] = a
        dic[abs(num-base**(a-1))] = a-1
        dic[abs(num-base**(a+1))] = a+1
        minimum = min(dic.keys())
        return dic[minimum]

print(closest_power(4,1))
print(closest_power(2,40))
print(closest_power(4,64))
print(closest_power(3,72))
        
        
