def rearrange_digits(input_list):
    def merge(array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            merge(left)
            merge(right)
            
            i,j = 0,0
            m = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[m] = right[j]
                    j += 1
                else:
                    array[m] = left[i]
                    i += 1
                m += 1
            
            while i < len(left):
                array[m] = left[i]
                i += 1
                m += 1
            
            while j < len(right):
                array[m] = right[j]
                j += 1
                m += 1        
    
        return array
    
    x,y = 0,0
    sorted_input_list = merge(input_list) 
    for i in range(len(sorted_input_list)):
        if i %2 == 0:
            x = x*10 + sorted_input_list[i] 
        else:
            y = y*10 + sorted_input_list[i]     
    return x,y
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[1, 0, 0, 0, 0, 0], [100, 000]]
test_function(test_case)

test_case = [[4, 6], [6, 4]]
test_function(test_case)

# list is only of one number
test_case = [[4], [4, 0]]
test_function(test_case)

#when list is empty
test_case = [[], [0, 0]]
test_function(test_case)

# numbers are repeated
test_case = [[4,1,2,4,4], [441, 42]]
test_function(test_case)
