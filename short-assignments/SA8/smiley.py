from cs1lib import *
from math import sqrt

class Smiley:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        # Draw face
        set_fill_color(1, 1, 0)
        draw_circle(self.x, self.y, self.size)

        # draw_mouth
        draw_circle(self.x, self.y, self.size // 2)

        # cover the upper part of mouth
        disable_stroke()
        draw_rectangle(self.x - (2 * self.size // 3), self.y - (2 * self.size // 3), (4 * self.size) // 3, 2 * self.size // 3)
        enable_stroke()

        # Draw eyes
        set_fill_color(0, 0, 0)
        draw_circle(self.x - self.size // 3, self.y - self.size // 3, self.size // 10)
        draw_circle(self.x + self.size // 3, self.y - self.size // 3, self.size // 10)


