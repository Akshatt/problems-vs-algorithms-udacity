def sqrt(number):
    if number == 0 or number ==1:
        return number
    
    left = 1
    right = number
    
    while left <= right:
        mid = (left + right)//2
        
        if mid*mid == number:
            return mid
        
        elif mid*mid < number:
            left = mid+1
            floored = mid
            
        else:
            right = mid - 1 

    return floored

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (7 == sqrt(50)) else "Fail")
print ("Pass" if  (6 == sqrt(48)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

