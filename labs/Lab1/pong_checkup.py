# Author: Thomas Monfre
# Date: 9/30/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program creates a game of Atari Pong for users to play.

from cs1lib import *

# CONSTANTS
# height and width of window and paddles, as well as how much the paddle moves with user input
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVEMENT = 40

# x locations for each paddle
LEFT_PADDLE_TOP_X = WINDOW_WIDTH - WINDOW_WIDTH
RIGHT_PADDLE_TOP_X = WINDOW_WIDTH - PADDLE_WIDTH

# keyboard inputs
LEFT_PADDLE_UP = "a"
LEFT_PADDLE_DOWN = "z"
RIGHT_PADDLE_UP = "k"
RIGHT_PADDLE_DOWN = "m"

# variables
# y locations of each paddle
left_paddle_top_y = WINDOW_HEIGHT - WINDOW_HEIGHT
right_paddle_top_y = WINDOW_HEIGHT - PADDLE_HEIGHT

# this function sets the background red and clears the screen, will be called in draw function
def draw_and_clear_background():
    set_clear_color(1, 0, 0)  # red
    clear()

# this function draws the left and right paddles, will be called in draw function
def draw_paddles():
    set_fill_color(0, 0, 1)  # blue
    draw_rectangle(LEFT_PADDLE_TOP_X, left_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # draw left paddle
    draw_rectangle(RIGHT_PADDLE_TOP_X, right_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # draw right paddle

# this function is passed to start_graphics. It clears the window and draws the paddles.
def draw():
    draw_and_clear_background()
    draw_paddles()

# this function is a callback function, called by key_press which is passed to start_graphics if user presses a key.
# this function moves the paddles up and down depending on user input as long as the paddle won't leave the screen.
def keypress(key):
    global left_paddle_top_y, right_paddle_top_y, first_drawing

    # moves left paddle up
    if key == LEFT_PADDLE_UP and left_paddle_top_y > 0:
        left_paddle_top_y = left_paddle_top_y - PADDLE_MOVEMENT

    # moves left paddle down
    if key == LEFT_PADDLE_DOWN and left_paddle_top_y < (WINDOW_HEIGHT - PADDLE_HEIGHT):
        left_paddle_top_y = left_paddle_top_y + PADDLE_MOVEMENT

    # moves right paddle up
    if key == RIGHT_PADDLE_UP and right_paddle_top_y > 0:
        right_paddle_top_y = right_paddle_top_y - PADDLE_MOVEMENT

    # moves right paddle down
    if key == RIGHT_PADDLE_DOWN and right_paddle_top_y < (WINDOW_HEIGHT - PADDLE_HEIGHT):
        right_paddle_top_y = right_paddle_top_y + PADDLE_MOVEMENT

start_graphics(draw, key_press=keypress)