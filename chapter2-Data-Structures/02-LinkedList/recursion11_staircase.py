# Problem Statement
# Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has n steps? Write a recursive function to solve the problem.

# Example:

# n == 1 then answer = 1

# n == 3 then answer = 4
# The output is 4 because there are four ways we can climb the staircase:

# 1 step + 1 step + 1 step
# 1 step + 2 steps
# 2 steps + 1 step
# 3 steps
# n == 5 then answer = 13

# Exercise - Write a recursive function to solve this problem

#Udacity Solution:
# Solution
## Read input as specified in the question.
## Print output as specified in the question.


def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


#My Solution:
"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""
def staircase(n):
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.
    
    # Recursive Step - Split the solution into base case if n > 3.
    return len(combos(n))


def combos(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1,1],[2]]
    if n == 3:
        return [[1,1,1],[1,2],[2,1],[3]]
    prev_l_nm1 = combos(n-1)
    prev_l_nm2 = combos(n-2)
    prev_l_nm3 = combos(n-3)
    out = [item + [1] for item in prev_l_nm1]
    out += [item + [2] for item in prev_l_nm2]
    out += [item + [3] for item in prev_l_nm3]
    return out    

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)

n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)