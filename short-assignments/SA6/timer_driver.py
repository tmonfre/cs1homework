# Author: Thomas Monfre
# Date: 10/18/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program tests the methods in the class Timer

from timer import Timer

# separates sections of print statements in the console to make it easier to view
def set_barrier():
    print("")
    print("***************")
    print("")

# create an example of the Timer class, starting at 00:01:30 and count down to 00:00:00
timer = Timer(1,30,0)

while not timer.is_zero():
    print(timer)
    timer.tick()

print(timer)

set_barrier()

# the following functions demonstrate that all methods in the Timer class work properly - same format as counter_driver

# creates three objects of class timer, an error message will print if initial value is not in range of 0 and the limit
timer1 = Timer(23, 22, 18)
timer2 = Timer(12, 60, 0)
timer3 = Timer(0, 0, 2)

# tests string method
print("String Method")
print(timer1)
print(timer2)
print(timer3)
print("")

# tests tick method
print("Tick Method: Timer 1")

print(timer1)
for i in range(0,3):
    timer1.tick()
    print(timer1)

set_barrier()

print("Tick Method: Timer 2")

print(timer2)
for i in range(0,3):
    timer2.tick()
    print(timer2)

set_barrier()

print("Tick Method: Timer 3")

print(timer3)
for i in range(0,3):
    timer3.tick()
    print(timer3)

set_barrier()

print("")

# tests is_zero method
print("Is Zero Method")

timer4 = Timer(0,0,0)
print(timer4.is_zero())

print(timer3.is_zero())