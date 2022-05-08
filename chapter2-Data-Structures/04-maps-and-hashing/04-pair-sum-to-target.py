# Problem statement
# Given an input_list and a target, return the pair of indices in the list that holds the values which sum to the target. For example,

# input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]

# Note

# The best solution takes O(n) time. This means that you cannot traverse the given list more than once. Hint - Think of an additional data structure that you should use here.
# You can assume that the list does not have any duplicates.

def pair_sum_to_target(input_list, target):
    # TODO: Write pair sum to target function
    d = dict()
    for idx, elm in enumerate(input_list):
        if target - elm in d.keys():  # and target - elm != elm:
            print([idx, d[target - elm]])
            return [idx, d[target - elm]]
        d.update({elm: idx})
    return [-1, -1]


def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)