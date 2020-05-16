def sort_012(input_list):
    front_index = 0
    back_index = len(input_list) - 1
    i = 0
    
    while i <= back_index: 
        
        if input_list[i] == 0:
            
            input_list[front_index], input_list[i]  = input_list[i], input_list[front_index]
            front_index += 1
            i += 1
        
        elif input_list[i] == 2:
                                
            input_list[i], input_list[back_index] =input_list[back_index], input_list[i]
            back_index -= 1
        
        else:
            i += 1
    
    return input_list 

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# already sorted
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# only 1s
test_function([1, 1, 1, 1, 1, 1])

# only 2s
test_function([2,2,2,2,2,2])

# only 0s
test_function([0, 0, 0, 0, 0, 0])

# empty 
test_function([])