# Author: Thomas Monfre
# Date: 11/8/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program, given a string of numbers and operation characters separate by spaces, computes their final
#          result using Reverse Polish Notation.

from stack import Stack

# split the string into a list of characters every time a space is encountered
def split_string(string):
    return string.split()

# depending on what operator is given, operate on the two values
def operate(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
    elif operator == "//":
        if y != 0:
            return x // y
        else:
            return "Cannot divide by zero"
    else:
        print(str(operator) + " is not a valid operator.")

# given a string of numbers and operators separated by spaces, perform Reverse Polish Notation and return final result
def compute_rpn(string):
    # create list of characters from the provided string by splitting the given string
    character_list = split_string(string)

    # create an empty stack using th  e class Stack
    stack = Stack()

    # go through list of characters, if the character is an integer, push it to the list, if it is an operator, pop
    # the previous two values from the stack and compute the given operation, then push the result back to the stack
    for i in character_list:
        if (i == "+" or i == "-" or i == "*" or i == "/" or i == "//") and not stack.is_empty():
            y = stack.pop()
            x = stack.pop()

            result = operate(x, y, i)
            stack.push(result)

        else:
            i = int(i)
            stack.push(i)

    # after each character in the list has been looped through, return the bottom (and only) value in the stack
    return int(stack.list[0])


print(compute_rpn("5 4 -"))
print(compute_rpn("5 13 1 - 4 / + 4 *"))
print(compute_rpn("1 3 2 - + 12 2 3 * // +"))
print(compute_rpn("3 8 + 2 *"))
print(compute_rpn("3 8 2 * +"))
print(compute_rpn("8 3 - 2 * 3 8 * + 9 -"))
print(compute_rpn("100 3325 2123 + / 12 2 3 - // +"))
print(compute_rpn("1 345 - 678 12 2 3  2 3 - // + 23 42 65 / * +"))