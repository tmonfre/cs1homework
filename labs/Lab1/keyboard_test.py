# Author: Thomas Monfre
# Date: 9/30/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program creates a game of Atari Pong for users to play.

from cs1lib import *

# constants

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_MOVEMENT = 40

LEFT_PADDLE_TOP_X = WINDOW_WIDTH - WINDOW_WIDTH
RIGHT_PADDLE_TOP_X = WINDOW_WIDTH - PADDLE_WIDTH

LEFT_PADDLE_UP = "a"
LEFT_PADDLE_DOWN = "z"
RIGHT_PADDLE_UP = "k"
RIGHT_PADDLE_DOWN = "m"

left_paddle_top_y = WINDOW_HEIGHT - WINDOW_HEIGHT
right_paddle_top_y = WINDOW_HEIGHT - PADDLE_HEIGHT

def draw_and_clear_background():
    set_clear_color(1, 0, 0)
    clear()

def draw_paddles():
    set_fill_color(0, 0, 1)
    draw_rectangle(LEFT_PADDLE_TOP_X, left_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(RIGHT_PADDLE_TOP_X, right_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)

def draw():
    draw_and_clear_background()
    draw_paddles()


def keypress(key):
    global left_paddle_top_y, right_paddle_top_y

    if key == LEFT_PADDLE_UP and left_paddle_top_y > 0:
        left_paddle_top_y = left_paddle_top_y - PADDLE_MOVEMENT

    if key == LEFT_PADDLE_DOWN and left_paddle_top_y < (WINDOW_HEIGHT - PADDLE_HEIGHT):
        left_paddle_top_y = left_paddle_top_y + PADDLE_MOVEMENT

    if key == RIGHT_PADDLE_UP and right_paddle_top_y > 0:
        right_paddle_top_y = right_paddle_top_y - PADDLE_MOVEMENT

    if key == RIGHT_PADDLE_DOWN and right_paddle_top_y < (WINDOW_HEIGHT - PADDLE_HEIGHT):
        right_paddle_top_y = right_paddle_top_y + PADDLE_MOVEMENT


start_graphics(draw, key_press=keypress)