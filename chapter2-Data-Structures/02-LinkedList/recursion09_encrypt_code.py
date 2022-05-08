# Problem statement
# In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, find out all the codes that are possible for a given input number.

# Example 1

# number = 123
# codes_possible = ["aw", "abc", "lc"]
# Explanation: The codes are for the following number:

# 1 . 23 = "aw"
# 1 . 2 . 3 = "abc"
# 12 . 3 = "lc"
# Example 2

# number = 145
# codes_possible = ["ade", "ne"]
# Return the codes in a list. The order of codes in the list is not important.

# Note: you can assume that the input number will not contain any 0s

# My solution:
def get_alphabet(number):
    return chr(number + 96)

def get_digits(number):
    digits = list()
    num = number
    while num != 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits, len(digits)

def get_alphabet_l_combo(combo):
    ab = list()
    for num in combo:
        if num > 26:
            return None
        print(get_alphabet(num))
        ab.append(get_alphabet(num))
    return ab
    
def all_combos(digits):
    if len(digits) == 1:
        return [digits]
    out = list()
    prev = all_combos(digits[:-1])
    
    for item in prev:
        out.append(item + [digits[-1]])
        last = item[-1]
        num = last * 10 + digits[-1]
        out.append(item[:-1] + [num])
    return out

def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    if number == 0:
        return [""]
    if number < 10:
        return [get_alphabet(number)]
    digits, n = get_digits(number)
    dgts = all_combos(digits)
    out = list()
    for item in dgts:
        print(item)
        res = get_alphabet_l_combo(item)
        if res is not None:
            out.append(''.join(res))
    return out

#--------------------------------
dgs, n = get_digits(1234)
print(f"dgs={dgs}, n={n}")
allcm = all_combos(dgs)
print(allcm)

get_alphabet_l_combo([12, 3, 14])

print(all_codes(123))

# Udacity Solution:
# Solution

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def all_codes(number):
    if number == 0:
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9 :
        
        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)
        
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
    
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    
    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)
    
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    
    return output



def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)

number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)