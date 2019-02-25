# Author: Thomas Monfre
# Date: 10/18/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class Timer that, given seconds, minutes, and hours creates a working timer that
#          counts down values via this system.

from counter import Counter

class Timer:
    # assigns hours, minutes, and seconds variables to objects within the Counter class
    # objects in the Counter class take limit, initial value, and minimum number of digits, thus the given values for
    # hours, minutes, and seconds become the initial values in the Counter object.
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    # returns a string for the current state of the timer, padded with zeros as appropriate
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.minutes)

    # this method always ticks the number of seconds when called
    # furthermore, it ticks the minutes if the seconds wrapped back and ticks the hours if the minutes wrapped back
    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    # this method returns True if the timer shows 00:00:00
    def is_zero(self):
        return ((self.hours.get_value() == 0) and (self.minutes.get_value() == 0) and (self.seconds.get_value() == 0))