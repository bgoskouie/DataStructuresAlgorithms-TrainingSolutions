# Longest-Consecutive-Subsequence

# Problem Statement
# Given a list of integers that contain natural numbers in random order. Write a program to find the longest possible sub sequence of consecutive numbers in the array. Return this subsequence in sorted order.

# In other words, you have to return the sorted longest (sub) list of consecutive numbers present anywhere in the given list.

# For example, given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5

# Note

# The solution must take O(n) time. Can you think of using a dictionary here?
# If two subsequences are of equal length, return the subsequence whose index of smallest element comes first.
# The Idea:
# Every element of the given input_list could be a part of some subsequence. Therefore, we need a way (using a dictionary) to keep track if an element has already been visited. Also, store length of a subsequence if it is maximum. For this purpose, we have to check in forward direction, if the (element+1) is available in the given dictionary, in a "while" loop. Similarly, we will check in backward direction for (element-1), in another "while" loop. At last, if we have the smallest element and the length of the longest subsequence, we can return a new list starting from "smallest element" to "smallest element + length".

# The steps would be:

# Create a dictionary, such that the elements of input_list become the "key", and the corresponding index become the "value" in the dictionary. We are creating a dictionary because the lookup time is considered to be constant in a dictionary.
# For each element in the input_list, first mark it as visited in the dictionary

# Check in forward direction, if the (element+1) is available. If yes, increment the length of subsequence

# Check in backward direction, if the (element-1) is available. If yes, increment the length of subsequence

# Keep a track of length of longest subsequence visited so far. For the longest subsequence, store the smallest element (say start_element) and its index as well.

# Return a new list starting from start_element to start_element + length.

def longest_consecutive_subsequence(input_list):
    total_min = None
    total_len = None
    d = dict.fromkeys(input_list, False)
    for elm in input_list:
        #d.update({elm: True})
        if d[elm]:
            continue
        d[elm] = True # visited
        subs_min = elm
        subs_len = 1
        newelm = elm + 1
        while newelm in d.keys():
            if d[newelm]:
                continue
            d[newelm] = True
            if newelm >= subs_min + subs_len:
                subs_len += 1
            newelm += 1
        newelm = elm - 1
        while newelm in d.keys():
            if d[newelm]:
                continue
            d[newelm] = True
            if newelm < subs_min:
                subs_min = newelm
                subs_len += 1
            newelm -= 1
        print((subs_min, subs_len))
        if total_len is None or total_len < subs_len:
            total_len = subs_len
            total_min = subs_min
        if total_len == subs_len:
            if total_min > subs_min:
                total_min = subs_min
       
    out = list(range(total_min,total_min+total_len,1))
    print(out)
    return out


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)


test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
test_function(test_case_2)


test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)




def longest_consecutive_subsequence(input_list):
    
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    element_dict = dict()

    # Traverse through the input_list, and populate the dictionary
    # Time complexity = O(n) 
    for index, element in enumerate(input_list):
        element_dict[element] = index

    # Represents the length of longest subsequence
    max_length = -1
    
    # Represents the index of smallest element in the longest subsequence
    starts_at = -1  

    # Traverse again - Time complexity = O(n) 
    for index, element in enumerate(input_list):

        current_starts = index
        element_dict[element] = -1         # Mark as visited

        current_count = 1                  # length of the current subsequence

        '''CHECK ONE ELEMENT FORWARD'''
        current = element + 1              # `current` is the expected number

        # check if the expected number is available (as a key) in the dictionary,
        # and it has not been visited yet (i.e., value > 0)
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        while current in element_dict and element_dict[current] > 0:
            current_count += 1             # increment the length of subsequence 
            element_dict[current] = -1     # Mark as visited
            current = current + 1          

            
        '''CHECK ONE ELEMENT BACKWARD'''
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        current = element - 1             # `current` is the expected number

        while current in element_dict and element_dict[current] > 0:    
            current_starts = element_dict[current]         # index of smallest element in the current subsequence
            current_count += 1                             # increment the length of subsequence 
            element_dict[current] = -1
            current = current - 1

        '''If length of current subsequence >= max length of previously visited subsequence'''
        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts            # index of smallest element in the current (longest so far) subsequence
            max_length = current_count            # store the length of current (longest so far) subsequence


    start_element = input_list[starts_at]          # smallest element in the longest subsequence

    # return a NEW list starting from `start_element` to `(start_element + max_length)` 
    return [element for element in range(start_element, start_element + max_length)]
