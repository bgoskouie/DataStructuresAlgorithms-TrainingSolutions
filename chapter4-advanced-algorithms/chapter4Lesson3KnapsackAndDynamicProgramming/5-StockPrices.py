# Stock Prices
# You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.

# For example, suppose you have the following prices:

# prices = [3, 4, 7, 8, 6]

# Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in this notebook.

# In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers in the array.

# The Idea
# The given array has the prices of a single stock at 13 different timestamps. The idea is to pick two timestamps: "buy_at_min" and "sell_at_max" such that the buy is made before a sell. We will use two pairs of indices while traversing the array:

# Pair 1 - This pair keeps track of our maximum profit while iterating over the list. It is done by storing a pair of indices - min_price_index, and max_price_index.
# Pair 2 - This pair keeps track of the profit between the lowest price seen so far and the current price while traversing the array. The lowest price seen so far is maintained with current_min_price_index.
# At each step we will make the greedy choice by choosing prices such that our profit is maximum. We will store the maximum of either of the two profits mentioned above.

# Exercise - Write the function definition here
# Fill out the function below and run it against the test cases. Take into consideration the time complexity of your solution.


# Babak's Solution:
def max_returns(prices):
    """
    Calculate maxiumum possible return
    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    min_price_index = 0
    max_price_index = 0
    current_min_price_index = 0
    for ind, p in enumerate(prices):
        d1 = prices[max_price_index] - prices[min_price_index]
        d2 = p - prices[current_min_price_index]
        if d2 > d1:
            min_price_index = current_min_price_index
            max_price_index = ind
        if p < prices[current_min_price_index]:
            current_min_price_index = ind
    return prices[max_price_index] - prices[min_price_index]

# Udacity Solution
def max_returns_udacity(arr):
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    if len(arr) < 2:
        return
    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit

# Test - Let's test your function
# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)
prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)
prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)
