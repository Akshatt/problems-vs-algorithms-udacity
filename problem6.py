def get_min_max(ints):
    if len(ints) == 0:
        return ()
    if len(ints) == 1:
        return ints[0], ints[0]
    else:
        mx = mn = ints[0]
        for i in ints:
            if i > mx:
                mx = i
            elif i < mn:
                mn = i
    
        return mn,mx



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print ("Pass" if ((11, 100) == get_min_max([32,45,56,78,54,32,11,100])) else "Fail")

# for list of same elements    
print ("Pass" if ((100, 100) == get_min_max([100, 100, 100, 100, 100])) else "Fail")

# for only one element
print ("Pass" if ((0,0) == get_min_max([0])) else "Fail")

# for zero elements
print ("Pass" if (() == get_min_max([])) else "Fail")
