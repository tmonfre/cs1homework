from smiley import Smiley
from random import randint, _sqrt

class Crowd:
    def __init__(self, n):
        self.slist = []

        for i in range(n):
            x = randint(0,400)
            y = randint(0,400)
            size = randint(50,100)

            self.slist.append(Smiley(x,y,size))

    def draw(self):
        for i in range(len(self.slist)):
            self.slist[i].draw()

    def remove_overlapping(self):
        for s1 in self.slist:
            for s2 in self.slist:
                if s1 != s2 and self.check_overlap(s1,s2):
                    self.slist.remove(s2)


    def check_overlap(self, s1, s2):
        distx = s1.x - s2.x
        disty = s1.y - s2.y

        dist = _sqrt(distx*distx + disty*disty)
        return dist < (s1.size + s2.size)