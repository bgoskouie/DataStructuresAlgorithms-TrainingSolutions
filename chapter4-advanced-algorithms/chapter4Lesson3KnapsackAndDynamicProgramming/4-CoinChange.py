# Coin Change
# You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# As an example:

# Input: coins = [1, 2, 3], amount = 6
# Output: 2
# Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use 3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.
# There's test code below that you can use to check your solution. And at the bottom of the notebook, you'll find two different possible solutions.


# Babak Solution:
def coin_change(coins, amount):
    # TODO: Complete the coin_change function
    # This should return one value: the fewest coins needed to make up the given amount
    coins = sorted(coins)
    out, num = coin_change_recur(coins, amount, 0)
    return num


def coin_change_recur(coins, delta, num):
    if delta == 0:
        return True, num
    if delta < 0:
        return False, -1
    found = False
    ind = len(coins) - 1
    while not found and ind >= 0:
        delta2 = delta - coins[ind]
        num2 = num + 1
        ret, num_out = coin_change_recur(coins, delta2, num2)
        if not ret:
            ind -= 1
        else:
            return True, num_out
    return False, -1

# Udacity Solution One:
# Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
# Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1
# Base Cases:
    # when Amount == 0: F(Amount) = 0
    # when Amount < 0: F(Amount) =  float('inf')
def coin_change_udacity1(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}

    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0
        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]
    res = return_change(amount)
    # return -1 when no change found
    return -1 if res == float('inf') else res

# Udacity Solution Two

# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.

def coin_change_udacity2(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')] * (amount + 1)
    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0
    i = 0
    while (i < amount):
        if res[i] != float('inf'):
            for coin in coins:
                if i <= amount - coin:
                    res[i+coin] = min(res[i] + 1, res[i+coin])
        i += 1
    if res[amount] == float('inf'):
        return -1
    return res[amount]


# print( coin_change([2, 3, 4, 5], 11))

def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)
arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)
arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
# Solutions
# Let's look at two different solutions. Here's one way to do it...

# Show Solution One

# And here's another possibility:

# Show Solution Two

