# Problem Statement
# Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

# For example:

# For input_string = "}}}}, the number of reversals required is 2.
# For input_string = "}{}}, the number of reversals required is 1.
# If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

# My Solution:
def minimum_bracket_reversals(input_string):
    def reverse(elm):
        if elm == "{":
            return "}"
        elif elm == "}":
            return "{"
        else:
            raise Exception("wtf")
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    # TODO: Write function here
    stack = Stack()
    for elm in input_string:
        if stack.top() == "{" and elm == "}":
            stack.pop()
        else:
            stack.push(elm)
    changes = 0
    closes = 0
    while not stack.is_empty():
        elm = stack.pop()
        if elm == "}":
            closes += 1
        elif elm == "{":
            if closes > 0:
                closes -= 1
            else:
                changes += 1
                closes += 1
        else:
            raise Exception("not acceptable input")
    if closes % 2 == 0:
        return changes  +  (closes // 2)
    else:
        return -1

#Solution:
def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            top = stack.top()
            if top != bracket:
                if top == '{':
                    stack.pop()
                    continue
            stack.push(bracket)

    ls = list()
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1
    return count


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]          
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]

test_function(test_case_1)

test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_2)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]

test_function(test_case_3)