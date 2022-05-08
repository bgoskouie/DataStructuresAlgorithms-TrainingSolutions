# kth largest element:
# Babak thinks the title should change to kth smallest element
# https://youtu.be/rhCx4vVJOwc    (Median problem)
# https://youtu.be/7DEYao1bEnE    (Basic Approach)
# https://youtu.be/UCs8HY6-FB0    (Search example)
# https://youtu.be/bw_bGIWQUII    (D&C High level)
# https://youtu.be/fjR5Y8iuMfI    (D&C Recursive Pivot)
# https://youtu.be/Wk5hEuBMvQc    (pseudocode)
# https://youtu.be/7tUR8nHKpXs    (median runtime)

# https://en.wikipedia.org/wiki/Median_of_medians

# Problem Statement
# Given an unsorted array Arr with n positive integers. Find the  𝑘𝑡ℎ  smallest element in the given array, using Divide & Conquer approach.

# Input: Unsorted array Arr and an integer k where  1≤𝑘≤𝑛 
# Output: The  𝑘𝑡ℎ  smallest element of array Arr

# Example 1
# Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
# k = 10
# Output = 99

# Example 2
# Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
# k = 5
# Output = 12

# The Pseudocode - fastSelect(Arr, k)
# Break Arr into  𝑛5  (actually it is  ⌈𝑛5⌉ ) groups, namely  𝐺1,𝐺2,𝐺3...𝐺𝑛/5 
# For each group  𝐺𝑖,∀1≤𝑖≤𝑛5 , do the following:
# Sort the group  𝐺𝑖 
# Find the middle position i.e., median  𝑚𝑖  of group  𝐺𝑖 
# Add  𝑚𝑖  to the set of medians  𝑆 
# The set of medians  𝑆  will become as  𝑆={𝑚1,𝑚2,𝑚3...𝑚𝑛/5} . The "good" pivot element will be the median of the set  𝑆 . We can find it as  𝑝𝑖𝑣𝑜𝑡=𝑓𝑎𝑠𝑡𝑆𝑒𝑙𝑒𝑐𝑡(𝑆,𝑛/10) .
# Partition the original Arr into three sub-arrays - Arr_Less_P, Arr_Equal_P, and Arr_More_P having elements less than pivot, equal to pivot, and bigger than pivot respectively.
# Recurse based on the sizes of the three sub-arrays, we will either recursively search in the small set, or the big set, as defined in the following conditions:

# If k <= length(Arr_Less_P), then return fastSelect(Arr_Less_P, k). This means that if the size of the "small" sub-array is at least as large as k, then we know that our desired  𝑘𝑡ℎ  smallest element lies in this sub-array. Therefore recursively call the same function on the "small" sub-array.


# If k > (length(Arr_Less_P) + length(Arr_Equal_P)), then return fastSelect(Arr_More_P, (k - length(Arr_Less_P) - length(Arr_Equal_P))). This means that if k is more than the size of "small" and "equal" sub-arrays, then our desired  𝑘𝑡ℎ  smallest element lies in "bigger" sub-array.


# Return pivot otherwise. This means that if the above two cases do not hold true, then we know that  𝑘𝑡ℎ  smallest element lies in the "equal" sub-array.

""" Babak's code """
import math
def fastSelect(Arr, k, calling_on_medians=False):
    '''input k is any number between 1 and n (=len(Arr))'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    # Break Arr into n/5 number of arrays (all in arrs list), all sorted!
    # "arrs"'s elements are arrays of G1, G2, G3,... Gn/5, their medians are also found in a list:
    arrs, medians = split_array_into_five_element_arrays(Arr, sort=True, find_medians=True)

    if len(medians) < 3 or calling_on_medians:
        # either the true median (if len=1 or 2) or an estimate of the median (when calling_on_medians==True)
        pivot = medians[0]
    else:
        # Start executing fastSelect with calling_on_medians=False, but
        # redo it here with calling_on_medians=True, on the next entrance, it wouldn't do the recursion!
        # otherwise the algorithm will be of order of n ** 2
        if not calling_on_medians:
            pivot = fastSelect(medians, math.ceil(len(medians)/2), calling_on_medians=True)
    # calling_on_medians is either True here or we have a pivot!
    arr_less_than_pivot = []
    arr_equal_to_pivot = []
    arr_more_than_pivot = []
    for elm in Arr:
        if elm < pivot:
            arr_less_than_pivot.append(elm)
        elif elm == pivot:
            arr_equal_to_pivot.append(elm)
        else:
            arr_more_than_pivot.append(elm)
    if k <= len(arr_less_than_pivot):
        return fastSelect(arr_less_than_pivot, k, calling_on_medians=False)
    elif k > len(arr_equal_to_pivot) + len(arr_less_than_pivot):
        return fastSelect(arr_more_than_pivot, k - len(arr_equal_to_pivot) - len(arr_less_than_pivot), calling_on_medians=False)
    elif k > len(arr_less_than_pivot) and k <= len(arr_equal_to_pivot) + len(arr_less_than_pivot):
        # terminating condition:
        return pivot
    else:
        raise Exception(f"k={k} is out of range!")

    a = 0

def split_array_into_five_element_arrays(Arr, sort=False, find_medians=False):
    def add_to_arrs(arrs, medians, grp, sort=False, find_medians=False):
        '''adds the array with five or less elements to arrs list'''
        if sort:
            grp.sort()
            if find_medians:
                # len(grp)=5  => ind=2,   len(grp)=4  => take ind=2
                medians.append(grp[len(grp)//2])     # grp[math.ceil(len(grp)/2) - 1])
        arrs.append(grp)
    arrs = []
    medians = []
    n = len(Arr)
    n_over_five = math.ceil(n/5)
    i_group = -1
    for i, elm in enumerate(Arr):
        if i // 5 == i / 5:
            i_group += 1
            if i_group != 0:
                add_to_arrs(arrs, medians, grp, sort=sort, find_medians=find_medians)
            grp = []  # There are maximum 5 number of elements in this list
        grp.append(elm)
    if len(grp) > 0:
        add_to_arrs(arrs, medians, grp, sort=sort, find_medians=find_medians)
    return arrs, medians
#---------------------------------------------------
#---------------------------------------------------
""" SOLUTION """
def fastSelect(Arr, k):                         # k is an index
    n = len(Arr)                                # length of the original array

    if (k > 0 and k <= n):                         # k should be a valid index
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0

        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):                     # n//5 gives the integer quotient of the division
            median = findMedian(Arr, 5*i, 5)    # find median of each group of size 5
            setOfMedians.append(median)
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5*i < n):
            median = findMedian(Arr, 5*i, n % 5)
            setOfMedians.append(median)

        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):            # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians)>1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians)//2))

        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element<pivot):
                Arr_Less_P.append(element)
            elif (element>pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)

        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))

        else:
            return pivot

# Helper function
def findMedian(Arr, start, size):
    myList = []
    for i in range(start, start + size):
        myList.append(Arr[i])

    # Sort the array
    myList.sort()

    # Return the middle element
    return myList[size // 2]
#---------------------------------------------------
#---------------------------------------------------
# testing subfunctions:
Arr = [6, 80, 15]
arrs, medians = split_array_into_five_element_arrays(Arr, sort=True, find_medians=True)
print(f"arrs={arrs}, medians={medians}")

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
arrs, medians = split_array_into_five_element_arrays(Arr, sort=False)
print(f"arrs={arrs}, medians={medians}")
arrs, medians = split_array_into_five_element_arrays(Arr, sort=True, find_medians=True)
print(f"arrs={arrs}, medians={medians}")
#---------------------------------------------------
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99


