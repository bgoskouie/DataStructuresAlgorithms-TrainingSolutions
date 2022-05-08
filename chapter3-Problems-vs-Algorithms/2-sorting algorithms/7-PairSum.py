# We saw a similar problem earlier in Data Structures course, Maps and Hashing lesson. There, we used an additional space to create a dictionary in order to solve the problem.
# Given an input array and a target value (integer), find two values in the array whose sum is equal to the target value. Solve the problem without using extra space. You can assume the array has unique values and will never have more than one solution.

# Babak's solution:
def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    d = dict()
    for elm in arr:
        # print("----------------")
        # print(d)
        # print(elm)
        if (elm, target-elm) in d.items():
            # print("success: (elm, target-elm) is in d.items()")
            ret = [elm, target-elm]
            ret.sort()
            # print(ret)
            return ret
        d.update({target - elm : elm})
    return [None, None]


# Solution:
def pair_sum(arr, target):
    # sort the list
    arr.sort()

    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]
        if front + back == target:
            return [front, back]
        elif front + back < target:       # sum < target ==> shift front pointer forward
            front_index += 1
        else:
            back_index -= 1               # sum > target ==> shift back pointer backward
    return [None, None]

def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")

input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)
# ----------------
# {}
# 2
# ----------------
# {7: 2}
# 7
# success: (elm, target-elm) is in d.items()
# [2, 7]
# Pass
input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)
# ----------------
# {}
# 0
# ----------------
# {9: 0}
# 8
# ----------------
# {9: 0, 1: 8}
# 5
# ----------------
# {9: 0, 1: 8, 4: 5}
# 7
# ----------------
# {9: 0, 1: 8, 4: 5, 2: 7}
# 9
# success: (elm, target-elm) is in d.items()
# [0, 9]
# Pass
input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
# ----------------
# {}
# 110
# ----------------
# {-101: 110}
# 9
# ----------------
# {-101: 110, 0: 9}
# 89
# Pass
