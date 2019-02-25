from smiley import Smiley
from random import randint
from math import sqrt

class Crowd2:
    def __init__(self, n):
        self.slist = []

        for i in range(n):
            x = randint(0,400)
            y = randint(0,400)
            r = randint(50,100)
            s = Smiley(x,y,r)

            self.slist.append(s)

    def draw(self):
        for s in self.slist:
            s.draw()

    def check_overlapping(self, s1, s2):
        distx = s1.x - s2.x
        disty = s1.y - s2.y

        total_dist = sqrt(distx*distx + disty*disty)

        return total_dist < s1.size + s2.size

    def remove_overlapping(self):
        for s1 in self.slist:
            for s2 in self.slist:
                if s1 != s2 and self.check_overlapping(s1,s2):
                    self.slist.remove(s2)