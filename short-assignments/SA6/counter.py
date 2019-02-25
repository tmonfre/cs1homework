# Author: Thomas Monfre
# Date: 10/18/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class Counter that, given a value and a limit, counts down from the value, then
#          loops back to one less than the limit when the counter reaches zero

class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        # assigns the limit and minimum number of digits to their respective instance variables
        self.limit = limit
        self.min_digits = min_digits

        # sets the value of the counter as the initial value if in range or one less than the limit if not in range
        if initial in range(0, limit + 1):
            self.counter = initial
        else:
            print("Initial counter value not in range. Counter value is now one less than the limit.")
            self.counter = limit - 1

    # returns the value of the counter
    def get_value(self):
        return self.counter

    # decrements the counter by one
    # if the counter is at 0 and the method tick is called, the counter value will become one less than the limit
    def tick(self):
        if self.counter == 0:
            self.counter = self.limit - 1
            return True
        else:
            self.counter = self.counter - 1
            return False

    # returns the counter padded with zeros as appropriate
    def __str__(self):
        length = len(str(self.counter))
        num_zeroes = self.min_digits - length # number of zeroes to pad
        return str('0' * num_zeroes) + str(self.counter)