def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    i = -1
    element = arr[i]
    while element == 9 and -i < len(arr):
        i -= 1
        element == arr[i]
    # Note list(range(-4,-1))   is  [-4, -3, -2]
    for i_ in range(i+1 , 0):
        arr[i_] = 0
    if arr[i] == 9:
        arr[i] = 0
        arr.insert(0, 1)
    else:
        arr[i] += 1
    return arr


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")


if __name__ == "__main__":
    # Test Case 1
    arr = [0]
    solution = [1]
    test_case = [arr, solution]
    test_function(test_case)

    # Test Case 2
    arr = [1, 2, 3]
    solution = [1, 2, 4]
    test_case = [arr, solution]
    test_function(test_case)

    # Test Case 3
    arr = [9, 9, 9]
    solution = [1, 0, 0, 0]
    test_case = [arr, solution]
    test_function(test_case)

    # Test Case 4
    arr = [5, 9, 9, 9]
    solution = [6, 0, 0, 0]
    test_case = [arr, solution]
    test_function(test_case)