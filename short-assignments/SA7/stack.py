# Author: Thomas Monfre
# Date: 11/8/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class Stack that is used to create a stack data structure (and will be used to
#          compute Reverse Polish Notation).

class Stack:
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0

    def __str__(self):
        return str(self.list)