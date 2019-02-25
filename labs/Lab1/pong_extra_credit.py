# Author: Thomas Monfre
# Date: 10/4/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program creates a game of Atari Pong for users to play. This version includes extra credit functions.

from cs1lib import *
from random import uniform

# constants for height and width of window and paddles, how much the paddle moves with user input, and radius of ball
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVEMENT = 12
BALL_RADIUS = 10

# constants for keyboard inputs
LEFT_PADDLE_UP = "a"
LEFT_PADDLE_DOWN = "z"
RIGHT_PADDLE_UP = "k"
RIGHT_PADDLE_DOWN = "m"
START_NEW_GAME = " "
QUIT = "q"

# constants for x locations for each paddle
LEFT_PADDLE_TOP_X = WINDOW_WIDTH - WINDOW_WIDTH
RIGHT_PADDLE_TOP_X = WINDOW_WIDTH - PADDLE_WIDTH

# state variables for y locations of each paddle
left_paddle_top_y = WINDOW_HEIGHT - WINDOW_HEIGHT
right_paddle_top_y = WINDOW_HEIGHT - PADDLE_HEIGHT

# state variables that determine whether or not the draw function should move the paddles up or down
# these variables are set true in the key_press callback function and false in the key_release callback function
# therefore they are only ever true when a user presses the corresponding key
key_left_paddle_up = False
key_left_paddle_down = False
key_right_paddle_up = False
key_right_paddle_down = False

# state variables for location, speed, and direction of the ball in the x and y directions
location_x = 200
location_y = 200
direction_x = 1
direction_y = 1
ball_speed = 5

# state variables to determine if it is the first time opening the program as well as if the game is over
first_drawing = True
game_over = False

# state variables to determine if the paddles are moving
left_paddle_moving = False
right_paddle_moving = False

# state variables for the red, green, and blue colors of the ball as well as for each paddle
r_ball = 1
g_ball = 1
b_ball = 1
r_paddle_left = 0
g_paddle_left = 1
b_paddle_left = 0
r_paddle_right = 0
g_paddle_right = 1
b_paddle_right = 0

# this function sets the background black and clears the screen, will be called in draw function
def draw_and_clear_background():
    set_clear_color(0, 0, 0)  # black
    clear()

# this function draws paddles, will be called in draw function
def draw_paddles():
    set_stroke_color(0, 0, 0) # black
    # draw left paddle
    set_fill_color(r_paddle_left, g_paddle_left, b_paddle_left)
    draw_rectangle(LEFT_PADDLE_TOP_X, left_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    # draw right paddle
    set_fill_color(r_paddle_right, g_paddle_right, b_paddle_right)
    draw_rectangle(RIGHT_PADDLE_TOP_X, right_paddle_top_y, PADDLE_WIDTH, PADDLE_HEIGHT)

# this function draws the ball and updates its location based on speed and direction
def draw_ball():
    global location_x, location_y

    set_fill_color(r_ball, g_ball, b_ball)
    set_stroke_color(0, 0, 0) # black
    draw_circle(location_x, location_y, BALL_RADIUS)

    location_x = location_x + (direction_x * ball_speed)
    location_y = location_y + (direction_y * ball_speed)

# this function determines if the ball goes out of bounds on either of the vertical walls and returns true if so
def out_of_bounds(x, boundary_left, boundary_right):
    if x > boundary_right or x < boundary_left:
        return True

# this function determines if the ball hits the top or bottom boundaries and returns true if so
def ball_hit_wall(y, boundary_top, boundary_bottom):
    if y > boundary_bottom or y < boundary_top:
        return True

# this function determines if the ball hit the left paddle and returns true if so
# the condition involving BALL_RADIUS ensures the outside of the ball hit the paddle
# the conditions involving ball_speed account for the frame rate of the draw function
# the condition involving direction ensures the ball is moving to the left
def ball_hit_left_paddle(x, y, paddle_top, paddle_bottom):
    if direction_x == -1 and x - BALL_RADIUS - ball_speed <= PADDLE_WIDTH - ball_speed and y in range(paddle_top - ball_speed, paddle_bottom + ball_speed):
        return True

# this function determines if the ball hit the right paddle and returns true if so
# the condition involving BALL_RADIUS ensures the outside of the ball hit the paddle
# the conditions involving ball_speed account for the frame rate of the draw function
# the condition involving direction ensures the ball is moving to the right
def ball_hit_right_paddle(x, y, paddle_top, paddle_bottom):
    if direction_x == 1 and x + BALL_RADIUS + ball_speed >= (WINDOW_WIDTH - PADDLE_WIDTH) + ball_speed and y in range(paddle_top - ball_speed, paddle_bottom + ball_speed):
        return True

# this function is passed to start_graphics. It clears the window, draws the paddles, and draws the ball.
def draw():
    global location_x, location_y, direction_x, direction_y, left_paddle_top_y, right_paddle_top_y, game_over, ball_speed, r_ball, g_ball, b_ball, r_paddle_left, g_paddle_left, b_paddle_left, r_paddle_right, g_paddle_right, b_paddle_right

    # draw welcome text if it's the first time the program has opened, as well as background and paddles
    # draw game-over text if the ball goes out of bounds
    # if neither of these are the case, then the game runs
    # whether or not the game is in progress is determined by user input of the space bar
    if first_drawing:
        clear()
        draw_and_clear_background()
        draw_paddles()

        set_font_size(30)
        set_font_bold()
        set_stroke_color(1, 1, 1) # white
        draw_text("Welcome to Pong", 72, 190)
        set_font_size(20)
        set_font_normal()
        draw_text("Press Space Bar to Begin", 83, 220)
    elif game_over:
        clear()
        draw_and_clear_background()
        draw_paddles()

        set_font_size(30)
        set_font_bold()
        set_stroke_color(1, 1, 1) # white
        draw_text("GAME OVER", 101, 190)
        set_font_size(20)
        set_font_normal()
        draw_text("Press Space Bar to Restart", 70, 220)
    else:
        draw_and_clear_background()
        draw_paddles()
        draw_ball()

    # the following if statements control the ball under various conditions/circumstances

    # ends the game if the ball goes out of bounds on right side
    # resets state variables of paddle color as well as ball location, speed, and color
    # determines new x and y directions depending on which direction(s) the ball went out of bounds
    if out_of_bounds(location_x + BALL_RADIUS + ball_speed, 0, 400):
        game_over = True
        location_x = 200
        location_y = 200
        ball_speed = 5
        direction_x = -1

        if direction_y > 0:
            direction_y = -1
        else:
            direction_y = 1

        r_ball = 1
        g_ball = 1
        b_ball = 1
        r_paddle_left = 0
        g_paddle_left = 1
        b_paddle_left = 0
        r_paddle_right = 0
        g_paddle_right = 1
        b_paddle_right = 0

    # ends the game if the ball goes out of bounds on right side
    # resets state variables of paddle color as well as ball location, speed, and color
    # determines new x and y directions depending on which direction(s) the ball went out of bounds
    if out_of_bounds(location_x - BALL_RADIUS - ball_speed, 0, 400):
        game_over = True
        location_x = 200
        location_y = 200
        ball_speed = 5
        direction_x = 1

        if direction_y > 0:
            direction_y = 1
        else:
            direction_y = -1

        r_ball = 1
        g_ball = 1
        b_ball = 1
        r_paddle_left = 0
        g_paddle_left = 1
        b_paddle_left = 0
        r_paddle_right = 0
        g_paddle_right = 1
        b_paddle_right = 0

    # reverses the y direction of the ball if it hits the bottom boundary
    if ball_hit_wall(location_y - BALL_RADIUS, 0.0, 400):
        direction_y = -direction_y

    # reverses the y direction of the ball if it hits the top boundary
    if ball_hit_wall(location_y + BALL_RADIUS, 0.0, 400):
        direction_y = -direction_y

    # reverses the x direction of the ball if it hits the left paddle & randomly changes the color of the ball & paddle
    if ball_hit_left_paddle(location_x, location_y, left_paddle_top_y, left_paddle_top_y + PADDLE_HEIGHT):
        direction_x = -direction_x
        r_ball = uniform(0.5, 1)
        g_ball = uniform(0.5, 1)
        b_ball = uniform(0.5, 1)
        r_paddle_left = uniform(0.5, 1)
        g_paddle_left = uniform(0.5, 1)
        b_paddle_left = uniform(0.5, 1)
        # increases the speed of the ball if the user is moving the paddle while the ball hits it
        # the boolean value for if the paddle is moving is set true in keypress event and false in keyrelease event
        if left_paddle_moving and ball_speed <= 10:
            ball_speed = ball_speed + 1

    # reverses the x direction of the ball if it hits the right paddle & randomly changes the color of the ball & paddle
    if ball_hit_right_paddle(location_x, location_y, right_paddle_top_y, right_paddle_top_y + PADDLE_HEIGHT):
        direction_x = -direction_x
        r_ball = uniform(0.5, 1)
        g_ball = uniform(0.5, 1)
        b_ball = uniform(0.5, 1)
        r_paddle_right = uniform(0.5, 1)
        g_paddle_right = uniform(0.5, 1)
        b_paddle_right = uniform(0.5, 1)
        # increases the speed of the ball if the user is moving the paddle while the ball hits it
        # the boolean value for if the paddle is moving is set true in keypress event and false in keyrelease event
        if right_paddle_moving and ball_speed <= 10:
            ball_speed = ball_speed + 1


    # the following if statements move the paddles up or down depending on if the user pressed the corresponding keys
    # the conditions of each if statement ensure each paddle won't leave the screen
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


# this function is a callback function, called by key_press which is passed to start_graphics if user presses a key
# this function changes boolean values for paddle movement to true if the user presses the corresponding key
# this function also starts a new game if user presses space bar and quits the entire program if user presses 'q'
def keypress(key):
    global key_left_paddle_up, key_left_paddle_down, key_right_paddle_up, key_right_paddle_down, first_drawing, first_drawing, game_over, left_paddle_moving, right_paddle_moving

    # moves left paddle up
    if key == LEFT_PADDLE_UP:
        key_left_paddle_up = True
        left_paddle_moving = True

    # moves left paddle down
    if key == LEFT_PADDLE_DOWN:
        key_left_paddle_down = True
        left_paddle_moving = True

    # moves right paddle up
    if key == RIGHT_PADDLE_UP:
        key_right_paddle_up = True
        right_paddle_moving = True

    # moves right paddle down
    if key == RIGHT_PADDLE_DOWN:
        key_right_paddle_down = True
        right_paddle_moving = True

    # starts new game
    if key == START_NEW_GAME:
        first_drawing = False
        game_over = False

    # quit program
    if key == QUIT:
        cs1_quit()

# this function is a callback function, called by key_release which is passed to start_graphics if user releases a key
# this function changes the boolean values for paddle movement to false after the user releases each corresponding key
def keyrelease(key):
    global key_left_paddle_up, key_left_paddle_down, key_right_paddle_up, key_right_paddle_down, left_paddle_moving, right_paddle_moving

    if key == LEFT_PADDLE_UP:
        key_left_paddle_up = False
        left_paddle_moving = False

    if key == LEFT_PADDLE_DOWN:
        key_left_paddle_down = False
        left_paddle_moving = False

    if key == RIGHT_PADDLE_UP:
        key_right_paddle_up = False
        right_paddle_moving = False

    if key == RIGHT_PADDLE_DOWN:
        key_right_paddle_down = False
        right_paddle_moving = False

# this function opens the graphics window and calls the draw function ~40 times per second
# when the user presses or releases a key, this function calls the callback functions keypress or keyrelease
start_graphics(draw, key_press=keypress, key_release=keyrelease, title="Pong")