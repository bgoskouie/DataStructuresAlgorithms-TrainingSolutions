
# What is Caching?
# Caching can be defined as the process of storing data into a temporary data storage to avoid recomputation or to avoid reading the data from a relatively slower part of memory again and again. Thus cachig serves as a fast "look-up" storage allowing programs to execute faster.

# Let's use caching to chalk out an efficient solution for a problem from the Recursion lesson.

# Problem Statement - (Recursion) - Repeat Exercise
# A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time. Given that the staircase has a total n steps, write a function to count the number of possible ways in which child can run up the stairs.

# For e.g.

# n == 1 then answer = 1

# n == 3 then answer = 4
# The output is 4 because there are four ways we can climb the staircase:

# 1 step + 1 step + 1 step
# 1 step + 2 steps
# 2 steps + 1 step
# 3 steps
# n == 5 then answer = 13

# Hint
# You would need to make use of the Inductive Hypothesis, which comprises of the following two steps:

# The Inductive Hypothesis: Calculate/assume the results for base case. In our problem scenario, the base cases would be when n = 1, 2, and 3.
# The Inductive Step: Prove that for every  𝑛>=3 , if the results are true for  𝑛  , then it holds for  (𝑛+1)  as well. In other words, assume that the statement holds for some arbitrary natural number  𝑛  , and prove that the statement holds for  (𝑛+1) .



def staircase(n):
    # Base Case - What holds true for minimum steps possible i.e., n == 1? Return the number of ways the child can climb one step.
    if n == 1:
        return 1
    # Inductive Hypothesis - What holds true for n == 2 or n == 3? Return the number of ways to climb them.
    if n == 2:
        return 2
    if n == 3:
        return 4
    # Inductive Step (n > 3) - use Inductive Hypothesis to formulate a solution
    
    ways = staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    return ways

test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)


cache = dict()
def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    numlist = [n - 1, n - 2, n - 3]
    sum = 0
    for num in numlist:
        if num in cache.keys():
            out = cache[num]
        else:
            out = staircase(num)
            cache.update({num: out})
        sum += out
    return sum


def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;
    return output

