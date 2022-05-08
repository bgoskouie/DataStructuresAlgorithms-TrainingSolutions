# Problem Statement
# You are given an array arr having n integers. You have to find the maximum sum of contiguous subarray among all the possible subarrays. This problem is commonly called as Maximum Subarray Problem. Solve this problem in O(nlogn) time, using Divide and Conquer approach.

# Example 1
# Input: arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
# Output: Maximum Sum = 10 for the subarray = [5, 0, 3, 2]

# Example 2
# Input: arr = [-2, -5, 6, -2, -3, 1, 5, -6]
# Output: Maximum Sum = 7 for the subarray = [6, -2, -3, 1, 5]

# As of now, let's not return the subarray itself.

# The Idea
# Divide the given array into three subarray w.r.t. the middle, say Left, Right, and Cross subarrays. Recurse on the Left part, and Right part untill you reach the base condition, i.e. single element in a subarray.

# Calculate the maximum sum of the Left, Right, and Cross subarrays, say L, R, and C respectively. Return the maximum of L, R, and C.

# Logic to Calculate C, the Maximum sum of a "Cross" Subarray
# Start from the middle index, and traverse (sum the elements) in the left direction. Keep track of the maximum sum on the left part, say leftMaxSum. Similarly, start from the (middle +1) index, and traverse (sum the elements) in the right direction. Keep track of the maximum sum on the right part, say rightMaxSum. Return the (leftMaxSum + rightMaxSum), as C. The following exmaple would help you imagine the solution better:

# Pseudocode and Time Complexity Analysis¶
# maxSubArrayRecursive(arr, start, stop)     T(n)
#   1. if (start==stop):
#       return arr[start]

#   2. Calculate mid index       constant

#   3. L = maxSubArrayRecursive(arr, start, mid)       T( 𝑛2 )

#   4. R = maxSubArrayRecursive(arr, mid+1, stop)       T( 𝑛2 )

#   5. C = maxCrossingSum(arr, start, mid, stop)         Θ(𝑛)

#   6. return max(C, max(L,R))       constant


# Total time of execution  𝑇(𝑛)  =  2∗𝑇(𝑛2)+Θ(𝑛)≡𝑂(𝑛𝑙𝑜𝑔𝑛)

def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.
    '''
    return maxSubArrayRecursive(arr, 0, len(arr) - 1)

def maxSubArrayRecursive(arr, start, stop):
    # index stop is included in the arr to look for the max
    if (start==stop):
        return arr[start]
    # Calculate mid index
    mid = (start + stop) // 2

    L = maxSubArrayRecursive(arr, start, mid)

    R = maxSubArrayRecursive(arr, mid+1, stop)
    # arr = [-2, 7, -6, 3, 1, -4, 5, 7]
    if start ==0 and stop == 7: #and mid == 1
        a = 0
    C = maxCrossingSum(arr, start, mid, stop)

    return max(C, max(L,R))

def maxCrossingSum(arr, start, mid, stop):
    if start > mid or stop < mid:
        raise Exception(f"Exception: {start} > {mid} or {stop} < {mid} is True")
    # The first element on each side must be included in the list
    maxL = arr[mid]
    maxR = arr[mid + 1]
    sum = maxL
    for ind in range(mid - 1, start - 1, -1):  # including start, excluding mid
        sum = sum + arr[ind]
        if sum < maxL:
            continue
        else:
            maxL = sum
    sum = maxR
    for ind in range(mid + 2, stop + 1, 1):  # including stop, , excluding mid + 1
        sum = sum + arr[ind]
        if sum < maxR:
            continue
        else:
            maxR = sum
    return maxL + maxR

# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 13

# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 6

# Test your code
arr = [-4, 14, -6, 7]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 15

# Test your code
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 10

# Test your code
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 7
