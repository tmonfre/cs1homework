# Author: Thomas Monfre
# Date: 9/27/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program creates a chalkboard (similar to MS Paint) for users to draw on.

from cs1lib import *

# state variables
red = 1
green = 1
blue = 1
old_x = 0  # previous x location of mouse click
old_y = 0  # previous y location of mouse click
stroke_size = 2
first_drawing = True  # used to draw black background once, and thus not cover any user drawings

# function passed to start_graphics to draw background and boxes that control stroke color and size
def draw():
    global first_drawing

    # clears graphics window with black once
    if first_drawing:
        set_clear_color(0, 0, 0)
        clear()
        first_drawing = False

    # draw box that when clicked changes stroke color to white
    set_stroke_width(1)
    set_stroke_color(0, 0, 0)
    set_fill_color(1,1,1)
    draw_rectangle(0, 370, 30, 30)

    # draw box that when clicked changes stroke color to black
    set_fill_color(0, 0, 0)
    draw_rectangle(30, 370, 30, 30)

    # draw box that when clicked changes stroke color to red
    set_fill_color(1, 0, 0)
    draw_rectangle(60, 370, 30, 30)

    # draw box that when clicked changes stroke color to green
    set_fill_color(0, 0.5, 0)
    draw_rectangle(90, 370, 30, 30)

    # draw box that when clicked changes stroke color to blue
    set_fill_color(0, 0, 1)
    draw_rectangle(120, 370, 30, 30)

    # draw box that when clicked changes stroke color to yellow
    set_fill_color(1, 1, 0)
    draw_rectangle(150, 370, 30, 30)

    # draw box that when clicked increases stroke size
    set_fill_color(1, 1, 1)
    draw_rectangle(180, 370, 30, 30)
    draw_text("+", 191, 390)

    # draw box that when clicked decreases stroke size
    draw_rectangle(210, 370, 30, 30)
    draw_text("-", 222, 390)

    # draw text above boxes that change stroke size
    set_stroke_color(1, 1, 1)
    draw_text("Change Stroke Color and Size", 30, 365)

# function called when the mouse is clicked, it replaces the old x and y coordinates with new ones
# this function also makes changes to the stroke size and color if the user clicks in the x and y ranges corresponding
# to the size of that box (boxes are drawn in the draw function)
def mouse_click(mx, my):
    global old_x, old_y, red, green, blue, stroke_size

    # replace old_x and old_y with location of mouse click
    old_x = mx
    old_y = my

    # change stroke color to white when clicked - corresponds to box in draw function
    if mx in range(0,30) and my in range(370, 400):
        red = 1
        green = 1
        blue = 1

    # change stroke color to black when clicked - corresponds to box in draw function
    if mx in range(30, 60) and my in range (370, 400):
        red = 0
        green = 0
        blue = 0

    # change stroke color to red when clicked - corresponds to box in draw function
    if mx in range(60, 90) and my in range (370, 400):
        red = 1
        green = 0
        blue = 0

    # change stroke color to green when clicked - corresponds to box in draw function
    if mx in range(90, 120) and my in range (370, 400):
        red = 0
        green = 0.5
        blue = 0

    # change stroke color to blue when clicked - corresponds to box in draw function
    if mx in range(120, 150) and my in range (370, 400):
        red = 0
        green = 0
        blue = 1

    # change stroke color to yellow when clicked - corresponds to box in draw function
    if mx in range(150, 180) and my in range (370, 400):
        red = 1
        green = 1
        blue = 0

    # increase stroke size - corresponds to box in draw function
    if mx in range(180, 210) and my in range (370, 400) and stroke_size < 10:
        stroke_size = stroke_size + 1

    # decrease stroke size - corresponds to box in draw function
    if mx in range(210, 240) and my in range (370, 400) and stroke_size > 0:
        stroke_size = stroke_size - 1

# function called when the mouse moves, draws stroke based on where user moves mouse (only if the mouse is pressed)
def mouse_move(mx, my):
    global old_x, old_y

    # draws line where user moves mouse only if the mouse is pressed
    if is_mouse_pressed():
        set_stroke_color(red, green, blue)
        set_stroke_width(stroke_size)
        draw_line(old_x, old_y, mx, my)
        old_x = mx
        old_y = my

# function called when different keys are pressed, used to change stroke color and size depending on key
def key_press(key):
    global red, green, blue, stroke_size

    # changes drawing color to red
    if key == "r":
        red = 1
        green = 0
        blue = 0

    # changes drawing color to green
    if key == "g":
        red = 0
        green = 0.5
        blue = 0

    # changes drawing color to blue
    if key == "b":
        red = 0
        green = 0
        blue = 1

    # changes drawing color to yellow
    if key == "y":
        red = 1
        green = 1
        blue = 0

    # changes drawing color to white
    if key == "w":
        red = 1
        green = 1
        blue = 1

    # changes drawing color to black (input key is e as in erase)
    if key == "e":
        red = 0
        green = 0
        blue = 0

    # increases stroke size
    if key == "+" and stroke_size < 10:
        stroke_size = stroke_size + 1

    # decreases stroke size
    if key == "-" and stroke_size > 0:
        stroke_size = stroke_size - 1


start_graphics(draw, mouse_press=mouse_click, mouse_move=mouse_move, key_press=key_press)