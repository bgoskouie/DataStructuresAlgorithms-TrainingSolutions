# Longest Common Subsequence
# In text analysis, it is often useful to compare the similarity of two texts (imagine if you were trying to determine plagiarism between a source and answer text). In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence (LCS).

# The Longest Common Subsequence is the longest sequence of letters that are present in both the given two strings in the same relative order.

# Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'. The LCS will be 'ABD' with the length as 3 letters. It is because each of the letters 'A' , 'B', and 'D' are present in both the given two strings in the same relative order. Note that:

# An LCS need not necessarily be a contiguous substring.
# There can be more than one LCS present in the given two strings.
# There can be many more common subsequences present here, with smaller length. But, in this problem we are concerned with the longest common subsequence.
# Dynamic Programming Approach - Storing Pre-Computed Values
# The LCS algorithm depends on looking at two strings and comparing them letter by letter. You can solve this problem in multiple ways. You can iterate through each letter in the strings and compare them, adding to your value for LCS as you go.

# Use a 2-D Matrix to Store the Relationship Between Letters of the Two Strings
# Recall that dynamic programming is all about breaking a larger problem into a smaller set of subproblems, and building up a complete result without having to repeat any subproblems. This approach assumes that you can split up a large LCS task into a combination of smaller LCS tasks. Let's look at the short example in more detail:

# A = 'ABCD'
# B = 'BD'
# We can see right away that letters B and D are in sequence in both the strings, therefore LCS is 'BD'. The length of the LCS here is 2.

# The Idea - We can calculate the LCS length by looking at relationships between each letter of the two strings. Let's make a matrix with the letters of first string on top and the letters of second string on the left side:


# This starts out as a matrix that has as many columns and rows as number of letters in the strings A and B plus 1, filled with zeros on the top and left sides. So, in this case, instead of a 2x4 matrix it is a 3x5. We can fill this matrix up by breaking it into smaller LCS problems. Start with first picking up one letter each from the given two strings, and then check if we have a common letter. Gradually, we will add up more letters from each string.

# Check Row 1
# The shortest subproblem: pick the starting letter of given two strings. We'll first ask, "what is the Longest Common Subsequence between these two letters 'A' and 'B'?" Here, the answer is zero and we fill in the corresponding grid cell with that value.


# Gradually, add up more letters from first string. The next question we'd ask, "what is the LCS between 'AB' and 'B'?" Here, we have a match, and can fill in the appropriate value 1.


# If we continue along this row, we can actually see that B only matches this one time, and any further questions, such as — What is the LCS between 'ABCD' and 'B'? — will have that same value, 1, due to the initial B-B match.


# Check Row 2
# Then, we move on to the second row. 'A' and 'BD' have 0 matches.


# We have 'AB' after picking one more letter from first string and 'BD' from second string, that have a B-B match, which we've already noted in the cell above. Gradually, we will add up more letters from first string, just like we did in the previous row. Finally, we have a match at the end D-D, where we can add 1 to our current highest match (1) to get a final LCS length as 2.


# The final LCS will have length as 2 letters.

# The Matrix Rules
# One thing to notice here is that, you can efficiently fill up this matrix one cell at a time. Each grid cell only depends on the values in the grid cells that are directly on top and to the left of it, or on the diagonal/top-left. The rules are as follows:

# Start with a matrix that has one extra row and column of zeros.
# As you traverse your string:
# If there is a match, fill that grid cell with the value to the top-left of that cell plus one. So, in our case, when we found a matching B-B, we added +1 to the value in the top-left of the matching cell, 0.
# If there is not a match, take the maximum value from either directly to the left or the top cell, and carry that value over to the non-match cell.

# After completely filling the matrix, the bottom-right cell will hold the non-normalized LCS length value.
# Calculate the length of longest common subsequence
# Implement the function lcs; this should calculate the length of longest common subsequence of characters between two strings.

def lcs(string_a, string_b):
    m = len(string_a) + 1
    n = len(string_b) + 1
    t = [[0] * n] * m
    # t[1][2] returns value at row 1 column 2
    # table is all filled in with 0s initially.
    i = 1  # row index
    j = 1  # column index
    #print(f"m={m},n={n}")
    for i in range(1, m):
        for j in range(1, n):
            #print(f"i={i},j={j}")
            if string_a[i - 1] == string_b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                #print(f"t[i][j - 1]={t[i][j - 1]},t[i - 1][j]={t[i - 1][j]},t[i][j]={t[i][j]}")
                t[i][j] = max([t[i][j - 1], t[i - 1][j]])
                #print(f"t[i][j]={t[i][j]}")
            #j += 1
        #i += 1
    return t[m - 1][n - 1]
# Hide Solution

def lcs_udacity_solution(string_a, string_b):

    # initialize the matrix
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):
        for char_b_i, char_b in enumerate(string_b):

            # If there is a match,
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1

            # If there is not a match,
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])
    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]
# Test your function on a few test strings by running the cell, below.

## Test cell
# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"
lcs_val1 = lcs(test_A1, test_B1)
test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"
lcs_val2 = lcs(test_A2, test_B2)
print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
# LCS val 1 =  5
# LCS val 2 =  7
# Tests passed!
# Time Complexity
# What is the time complexity of the above implementation?

# Hide Solution

'''
The time complexity of the above implementation is dominated by the two nested loops,
Let the length of string_a and string_b is `n` and `m` respectively.
This would lead to a time complexity of O(n*m).
But, in general, we can consider it as O(n*n) instead of O(n*m).
'''
