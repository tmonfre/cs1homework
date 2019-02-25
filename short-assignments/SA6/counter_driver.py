# Author: Thomas Monfre
# Date: 10/18/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program tests the methods in the class Counter

from counter import Counter

# separates sections of print statements in the console to make it easier to view
def set_barrier():
    print("")
    print("***************")
    print("")

# create two objects of class counter, an error message will print if initial value is not in range of 0 and the limit
counter1 = Counter(60, 2, 4)
counter2 = Counter(45, -2, 1)

set_barrier()

# tests get_value method
print("get_value Method: ")
print(counter1.get_value())
print(counter2.get_value())

set_barrier()

# tests string method
print("__str__ Method: ")
print(counter1)
print(counter2)

set_barrier()

# tests tick method
print("Tick Method: ")

print("Tick counter1 three times:")

for i in range(0,3):
    counter1.tick()
    print(counter1)

print("Tick counter2 four times:")

for i in range (0,4):
    counter2.tick()
    print(counter2)
