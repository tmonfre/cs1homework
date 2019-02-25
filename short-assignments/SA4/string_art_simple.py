# Author: Thomas Monfre
# Date: 9/22/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program draws string art based on two lines of equal length with string (lines) attached between them.

from cs1lib import *

def set_background():
    set_clear_color(0, 0, 0)
    clear()

# coordinates of endpoints for Stick A
x1a = 50
y1a = 100
x2a = 175
y2a = 325

# coordinates of endpoints for Stick B
x1b = 345
y1b = 125
x2b = 305
y2b = 250

def stick_1():
    set_stroke_width(3)
    set_stroke_color(1, 1, 1)
    draw_line(x1a, y1a, x2a, y2a)

def stick_2():
    set_stroke_width(3)
    set_stroke_color(1, 1, 1)
    draw_line(x1b, y1b, x2b, y2b)

def string_1():
    set_stroke_width(1)
    set_stroke_color(1, 1, 1)
    draw_line(x1a, y1a, x2b, y2b)

def string_2():
    set_stroke_color(1, 1, 1)
    draw_line(((x2a - x1a) / 2) + x1a, ((y2a - y1a) / 2) + y1a, ((x2b - x1b) / 2) + x1b, ((y2b - y1b) / 2) + y1b)

def string_3():
    set_stroke_color(1, 1, 1)
    draw_line(x2a, y2a, x1b, y1b)


def main():
    set_background()
    stick_1()
    stick_2()
    string_1()
    string_2()
    string_3()

start_graphics(main)