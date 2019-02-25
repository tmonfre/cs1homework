# Author: Thomas Monfre
# Date: 10/2/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program creates a game of Atari Pong for users to play. This checkpoint only features the moving paddles

from cs1lib import *

# constants for height and width of window and paddles, as well as how much the paddle moves with user input
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVEMENT = 10

# constants for x locations for each paddle
LEFT_PADDLE_TOP_X = WINDOW_WIDTH - WINDOW_WIDTH
RIGHT_PADDLE_TOP_X = WINDOW_WIDTH - PADDLE_WIDTH

# constants for keyboard inputs
LEFT_PADDLE_UP = "a"
LEFT_PADDLE_DOWN = "z"
RIGHT_PADDLE_UP = "k"
RIGHT_PADDLE_DOWN = "m"

# state variables for y locations of each paddle
left_paddle_top_y = WINDOW_HEIGHT - WINDOW_HEIGHT
right_paddle_top_y = WINDOW_HEIGHT - PADDLE_HEIGHT

# state variables that determine whether or not the draw function should move the paddles up or down
# these variables are set true in the key_press callback function and false in the key_release callback function
# therefore they only ever hold the value true when a user presses the corresponding key
key_left_paddle_up = False
key_left_paddle_down = False
key_right_paddle_up = False
key_right_paddle_down = False

# this function sets the background black and clears the screen, will be called in draw function
def draw_and_clear_background():
    set_clear_color(0, 0, 0)  # black
    clear()

# this function draws the left and right paddles, will be called in draw function
def draw_paddles():
    set_fill_color(0, 1, 0)  # green
    draw_rectangle(LEFT_PADDLE_TOP_X, left_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # draw left paddle
    draw_rectangle(RIGHT_PADDLE_TOP_X, right_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # draw right paddle

# this function is passed to start_graphics. It clears the window and draws the paddles.
def draw():
    global left_paddle_top_y, right_paddle_top_y

    draw_and_clear_background()
    draw_paddles()

    # the following if statements move the paddles up or down depending on if the user pressed the corresponding keys
    # the conditions of each if-statement ensure each paddle won't leave the screen
    # the boolean values are set true when the user presses the correct key and set false when the user releases the key
    # in the respective callback functions below
    if key_left_paddle_up and left_paddle_top_y > 0:
        left_paddle_top_y = left_paddle_top_y - PADDLE_MOVEMENT

    if key_left_paddle_down and left_paddle_top_y < (WINDOW_HEIGHT - PADDLE_HEIGHT):
        left_paddle_top_y = left_paddle_top_y + PADDLE_MOVEMENT

    if key_right_paddle_up and right_paddle_top_y > 0:
        right_paddle_top_y = right_paddle_top_y - PADDLE_MOVEMENT

    if key_right_paddle_down and right_paddle_top_y < (WINDOW_HEIGHT - PADDLE_HEIGHT):
        right_paddle_top_y = right_paddle_top_y + PADDLE_MOVEMENT

# this function is a callback function, called by key_press which is passed to start_graphics if user presses a key.
# this function changes boolean values for paddle movement to true if the user presses the corresponding key
def keypress(key):
    global key_left_paddle_up, key_left_paddle_down, key_right_paddle_up, key_right_paddle_down

    # moves left paddle up
    if key == LEFT_PADDLE_UP:
        key_left_paddle_up = True

    # moves left paddle down
    if key == LEFT_PADDLE_DOWN:
        key_left_paddle_down = True

    # moves right paddle up
    if key == RIGHT_PADDLE_UP:
        key_right_paddle_up = True

    # moves right paddle down
    if key == RIGHT_PADDLE_DOWN:
        key_right_paddle_down = True

# this function is a callback function, called by key_release which is passed to start_graphics if user releases a key
# this function changes the boolean values for paddle movement to false after the user releases each corresponding key
def keyrelease(key):
    global key_left_paddle_up, key_left_paddle_down, key_right_paddle_up, key_right_paddle_down

    if key == LEFT_PADDLE_UP:
        key_left_paddle_up = False

    if key == LEFT_PADDLE_DOWN:
        key_left_paddle_down = False

    if key == RIGHT_PADDLE_UP:
        key_right_paddle_up = False

    if key == RIGHT_PADDLE_DOWN:
        key_right_paddle_down = False

# this function opens the graphics window and calls the draw function ~40 times per second
# when the user presses or releases a key, this function calls the callback functions keypress or keyrelease
start_graphics(draw, key_press=keypress, key_release=keyrelease, title="Pong Checkpoint")