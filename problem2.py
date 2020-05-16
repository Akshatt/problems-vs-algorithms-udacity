def rotated_array_search(input_list, number):
    left = 0
    right = len(input_list) - 1
    
    while left <= right:
        mid = (left+right)//2
       
        if input_list[mid] == number:
            return mid
        
        if input_list[left] <= input_list[mid]:
            if number >= input_list[left] and number <= input_list[mid]:
                right = mid -1 
            else:
                left = mid + 1 
            continue

        if input_list[mid] <= input_list[right]:
            if number <= input_list[right] and input_list[mid] <= number:
                left = mid + 1 
            else:
                right = mid -1  
            continue
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# testing with only one value rotated 
test_function([[2, 3, 4, 6, 7, 8, 9, 10, 1], 1])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

test_function([[6, 7, 7, 8, 1, 2, 3, 4], 8])

# testing for duplicate target number
test_function([[6, 7, 8, 1, 1, 2, 3, 4], 1])

# testing with multiple duplicate values
test_function([[6, 7, 7, 8, 8, 1, 2, 3, 4], 10])

# testing with an empty list
test_function([[], 1])

