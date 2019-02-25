# Author: Thomas Monfre
# Date: 9/25/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program draws string art based on two lines of equal length with string (lines) attached between them.

from cs1lib import *

def set_background():
    set_clear_color(0, 0, 0)
    clear()

# the following function draws the line art, it will be called in main() which is passed to start_graphics()
def draw_line_art(x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b, num):
    set_background()

    # draws first big stick from which the strings attach
    def draw_stick_A():
        set_stroke_width(3)
        set_stroke_color(0, 0.5, 1)
        draw_line(x1a, y1a, x2a, y2a)

    # draws second big stick from which the strings attach
    def draw_stick_B():
        set_stroke_width(3)
        set_stroke_color(0, 0.5, 1)
        draw_line(x1b, y1b, x2b, y2b)

    draw_stick_A()
    draw_stick_B()

    WIDTH = 1 / (num - 1)  # fraction of stick length between each string (constant determined by input for num)
    f = 0  # placeholder for fraction of distance from endpoint of stick to new string, used in header of while loop

    # the following while-loop repeats to draw strings at a set interval (WIDTH)
    while f <= 1:
        set_stroke_width(1)
        set_stroke_color(0, (1 * f), 1)
        draw_line(x1a + (f * (x2a - x1a)), y1a + (f * (y2a - y1a)), x2b - (f * (x2b - x1b)), y2b - (f * (y2b - y1b)))
        f = f + WIDTH

# main function that is passed to start_graphics (puts everything together)
def main():
    draw_line_art(50, 100, 175, 325, 345, 125, 305, 250, 35)

start_graphics(main, title="String Art")