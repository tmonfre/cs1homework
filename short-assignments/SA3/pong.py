from cs1lib import *
# pong.py
# Solution to CS 1 Lab Assignment #1.
# Written by Peter Johnson, updated for cs1lib by Devin Balkcom.
# Major changes by THC.
# Plays a game of pong.  A ball bounces around, and paddles move
# up and down to meet the ball.  Whenever the ball hits the left or
# right wall, the game is over.  Whenever the ball hits the top or
# bottom wall, it bounces off the wall.  Whenever the ball hits a
# paddle, it bounces off the paddle.
# Pressing 'a' moves the left paddle up.
# Pressing 'z' moves the left paddle down.
# Pressing 'k' moves the right paddle up.
# Pressing 'm' moves the right paddle down.
# Pressing the space bar starts a new game.
# Pressing 'q' quits the program.

from cs1lib import *

# Constants for the keys that matter.
RESTART_KEY = ' '
QUIT_KEY = 'q'
LEFT_PADDLE_UP_KEY = 'a'
LEFT_PADDLE_DOWN_KEY = 'z'
RIGHT_PADDLE_UP_KEY = 'k'
RIGHT_PADDLE_DOWN_KEY = 'm'

PADDLE_HEIGHT = 80          # paddle height, in pixels
PADDLE_WIDTH = 20           # paddle width, in pixels
PADDLE_MOVE_SPEED = 10      # how many pixels paddles move per frame

WINDOW_WIDTH = 400          # in pixels
WINDOW_HEIGHT = 400         # in pixels
WINDOW_HORIZ_CENTER = WINDOW_WIDTH // 2  # x-coordinate of window center
WINDOW_VERT_CENTER = WINDOW_HEIGHT // 2  # y-coordinate of window center

BALL_RADIUS = 10            # in pixels
INITIAL_HORIZ_VELOCITY = 3  # the ball's initial horizontal velocity
INITIAL_VERT_VELOCITY = 3   # the ball's initial vertical velocity

WALL_THICKNESS = 5          # thickness of each wall, in pixels

# The leftmost coordinates of the two paddles.
LEFT_PADDLE_X = WALL_THICKNESS
RIGHT_PADDLE_X = WINDOW_WIDTH - WALL_THICKNESS - PADDLE_WIDTH

# The inner x-coordinates of the two paddles.
LEFT_PADDLE_RIGHT = LEFT_PADDLE_X + PADDLE_WIDTH
RIGHT_PADDLE_LEFT = RIGHT_PADDLE_X

# Locations of wall sides and wall dimensions.
TOP_WALL_TOP = 0
TOP_WALL_BOTTOM = WALL_THICKNESS
HORIZ_WALL_LEFT = 0
HORIZ_WALL_RIGHT = WINDOW_WIDTH
HORIZ_WALL_WIDTH = WINDOW_WIDTH
HORIZ_WALL_HEIGHT = WALL_THICKNESS
BOTTOM_WALL_TOP = WINDOW_HEIGHT - WALL_THICKNESS
LEFT_WALL_LEFT = 0
LEFT_WALL_RIGHT = WALL_THICKNESS
VERT_WALL_TOP = WALL_THICKNESS
VERT_WALL_BOTTOM = WINDOW_HEIGHT - WALL_THICKNESS
VERT_WALL_WIDTH = WALL_THICKNESS
VERT_WALL_HEIGHT = WINDOW_HEIGHT - 2 * WALL_THICKNESS
RIGHT_WALL_LEFT = WINDOW_WIDTH - WALL_THICKNESS

# Determine whether a horizontal line segment and a vertical line segment intersect.
# The horizontal segment's endpoints are at x-coordinates horiz_left and horiz_right,
# and its y-coordinate is horiz_y.  The vertical segment's endpoints are at
# y-coordinates vert_top and vert_bottom, and its x-coordinate is vert_x.
# The segments intersect if the x-coordinate of the vertical line is between the
# endpoints of the horizontal line AND the y-coordinate of the horizontal line is between
# the endpoints of the vertical line.
def segments_intersect(horiz_left, horiz_right, horiz_y, vert_x, vert_top, vert_bottom):
    return horiz_left <= vert_x <= horiz_right and vert_top <= horiz_y <= vert_bottom

# Determine whether the ball touches a vertical line segment.
def ball_touches_vert_segment(ball_x, ball_y, vert_x, vert_top, vert_bottom):
    # Does a horizontal line segment going through the center of the ball intersect
    # the vertical line segment?
    return segments_intersect(ball_x - BALL_RADIUS, ball_x + BALL_RADIUS, ball_y,
                              vert_x, vert_top, vert_bottom)
 
# Determine whether the ball touches a horizontal line segment.
def ball_touches_horiz_segment(ball_x, ball_y, horiz_left, horiz_right, horiz_y):
    # Does a vertical line segment going through the center of the ball intersect
    # the horizontal line segment?
    return segments_intersect(horiz_left, horiz_right, horiz_y, ball_x,
                              ball_y - BALL_RADIUS, ball_y + BALL_RADIUS)
    
# Draw the background, including the walls.
def draw_background():
    set_clear_color(1, 1, 0.375)    # light yellow
    clear()
    
    # Draw the left and right walls in red.
    set_fill_color(1, 0, 0)
    draw_rectangle(LEFT_WALL_LEFT, VERT_WALL_TOP, VERT_WALL_WIDTH, VERT_WALL_HEIGHT)
    draw_rectangle(RIGHT_WALL_LEFT, VERT_WALL_TOP, VERT_WALL_WIDTH, VERT_WALL_HEIGHT)

    # Draw the top and bottom walls in blue.
    set_fill_color(0, 0, 1)
    draw_rectangle(HORIZ_WALL_LEFT, TOP_WALL_TOP, HORIZ_WALL_WIDTH, HORIZ_WALL_HEIGHT)
    draw_rectangle(HORIZ_WALL_LEFT, BOTTOM_WALL_TOP, HORIZ_WALL_WIDTH, HORIZ_WALL_HEIGHT)

# Return the position of a paddle, based on its current position, whether a particular
# key has been pressed, and the distance to move the paddle if the key is pressed.
def position_paddle(current_position, key_pressed, distance):
    if key_pressed:
        # If the key is pressed, determine the new position.
        new_position = current_position + distance

        # If the new position keeps the paddle within the horizontal walls, return
        # the new position.  Otherwise, return the current position.
        if new_position >= TOP_WALL_BOTTOM and new_position + PADDLE_HEIGHT <= BOTTOM_WALL_TOP:
            return new_position
        else:
            return current_position
    else:
        return current_position     # leave position alone if key not pressed

# Put the ball in the middle of the window.   
def center_ball():
    global ball_x, ball_y
    
    ball_x = WINDOW_HORIZ_CENTER
    ball_y = WINDOW_VERT_CENTER
    
# Start the game.
def start_game():
    global ball_x_velocity, ball_y_velocity
    global game_in_progress
    ball_x_velocity = INITIAL_HORIZ_VELOCITY
    ball_y_velocity = INITIAL_VERT_VELOCITY
    game_in_progress = True
    
# Halt the game.
def stop_game():
    global game_in_progress
    game_in_progress = False

# Record that a key was pressed.
def key_down(key):
    global pressed_left_paddle_up, pressed_left_paddle_down, pressed_right_paddle_up, pressed_right_paddle_down
    global pressed_quit, pressed_restart

    if key == LEFT_PADDLE_UP_KEY:
        pressed_left_paddle_up = True
    elif key == LEFT_PADDLE_DOWN_KEY:
        pressed_left_paddle_down = True
    elif key == RIGHT_PADDLE_UP_KEY:
        pressed_right_paddle_up = True
    elif key == RIGHT_PADDLE_DOWN_KEY:
        pressed_right_paddle_down = True
    elif key == QUIT_KEY:
        pressed_quit = True
    elif key == RESTART_KEY:
        pressed_restart = True

# Record that a key was released.
def key_up(key):
    global pressed_left_paddle_up, pressed_left_paddle_down, pressed_right_paddle_up, pressed_right_paddle_down
    global pressed_quit, pressed_restart

    if key == LEFT_PADDLE_UP_KEY:
        pressed_left_paddle_up = False
    elif key == LEFT_PADDLE_DOWN_KEY:
        pressed_left_paddle_down = False
    elif key == RIGHT_PADDLE_UP_KEY:
        pressed_right_paddle_up = False
    elif key == RIGHT_PADDLE_DOWN_KEY:
        pressed_right_paddle_down = False
    elif key == QUIT_KEY:
        pressed_quit = False
    elif key == RESTART_KEY:
        pressed_restart = False

# STATE VARIABLES:

# Start both paddles at the top.
left_paddle_y = TOP_WALL_TOP + HORIZ_WALL_HEIGHT
right_paddle_y = TOP_WALL_TOP + HORIZ_WALL_HEIGHT

# Are the keys pressed?
pressed_left_paddle_up = False
pressed_left_paddle_down = False
pressed_right_paddle_up = False
pressed_right_paddle_down = False
pressed_quit = False
pressed_restart = False

# Set up the rest of the initial state.
center_ball()
stop_game()

# Main function.  Plays the game.
def main():
    global ball_x, ball_y, ball_x_velocity, ball_y_velocity
    global left_paddle_y, right_paddle_y
    global game_in_progress

    # Aesthetics.
    disable_stroke()

    # Are we done?
    if pressed_quit:
        cs1_quit()
    elif pressed_restart:
        # Start a game.
        center_ball()
        start_game()

    draw_background()

    # Draw the paddles.
    set_fill_color(0, 0.5, 0)   # dark green
    draw_rectangle(LEFT_PADDLE_X, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(RIGHT_PADDLE_X, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Draw the ball.
    set_fill_color(0.5, 0, 0.25)    # purple
    draw_circle(ball_x, ball_y, BALL_RADIUS)

    # If no game in progress, tell user how to start.
    if not game_in_progress:
        enable_stroke()

        # The string saying how to start the game.
        GAME_START_MSG = "Press the space key to start a game"

        # Constants for the size and location of the game start message.
        GAME_START_MSG_WIDTH = get_text_width(GAME_START_MSG)  # in pixels
        GAME_START_MSG_X = WINDOW_HORIZ_CENTER - GAME_START_MSG_WIDTH // 2
        GAME_START_MSG_Y = 3 * WINDOW_HEIGHT // 4

        draw_text(GAME_START_MSG, GAME_START_MSG_X, GAME_START_MSG_Y)
        disable_stroke()

    # End the game if the ball touches a vertical wall.
    if ball_touches_vert_segment(ball_x, ball_y, LEFT_WALL_RIGHT,
                                 VERT_WALL_TOP, VERT_WALL_BOTTOM) or \
        ball_touches_vert_segment(ball_x, ball_y, RIGHT_WALL_LEFT,
                                  VERT_WALL_TOP, VERT_WALL_BOTTOM):
        stop_game()

    # Negate x velocity if the ball touches a vertical paddle surface,
    # but also move it a ball radius away from the paddle so that we don't
    # get caught oscillating the x-velocity.
    elif ball_touches_vert_segment(ball_x, ball_y, LEFT_PADDLE_RIGHT,
                                   left_paddle_y, left_paddle_y + PADDLE_HEIGHT) or \
        ball_touches_vert_segment(ball_x, ball_y, RIGHT_PADDLE_LEFT,
                                  right_paddle_y, right_paddle_y + PADDLE_HEIGHT):
        ball_x_velocity = - ball_x_velocity
        if ball_x > WINDOW_HORIZ_CENTER:
            ball_x = RIGHT_PADDLE_LEFT - BALL_RADIUS    # move away from right paddle
        else:
            ball_x = LEFT_PADDLE_RIGHT + BALL_RADIUS    # move away from left paddle

    # Negate y velocity if the ball touches a horizontal wall.
    if ball_touches_horiz_segment(ball_x, ball_y, HORIZ_WALL_LEFT, HORIZ_WALL_RIGHT,
                                  TOP_WALL_BOTTOM) or \
        ball_touches_horiz_segment(ball_x, ball_y, HORIZ_WALL_LEFT, HORIZ_WALL_RIGHT,
                                   BOTTOM_WALL_TOP):
        ball_y_velocity = - ball_y_velocity

    # If the game is in progress, update the ball's position in both directions.
    if game_in_progress:
        ball_x = ball_x + ball_x_velocity
        ball_y = ball_y + ball_y_velocity

    # Move the paddles appropriately, but never let them go beyond the horizontal walls.
    left_paddle_y = position_paddle(left_paddle_y, pressed_left_paddle_up, -PADDLE_MOVE_SPEED)
    left_paddle_y = position_paddle(left_paddle_y, pressed_left_paddle_down, PADDLE_MOVE_SPEED)
    right_paddle_y = position_paddle(right_paddle_y, pressed_right_paddle_up, -PADDLE_MOVE_SPEED)
    right_paddle_y = position_paddle(right_paddle_y, pressed_right_paddle_down, PADDLE_MOVE_SPEED)

start_graphics(main, title = "Pong", width = WINDOW_WIDTH, height = WINDOW_HEIGHT,
               key_press = key_down, key_release = key_up, framerate = 50)
