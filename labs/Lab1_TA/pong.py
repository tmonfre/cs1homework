from cs1lib import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80

L_PADDLE_X = 0
R_PADDLE_X = WINDOW_WIDTH - PADDLE_WIDTH

l_paddle_y = 0
r_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT

PADDLE_MOVEMENT_VALUE = 10

l_paddle_up = False
l_paddle_down = False
r_paddle_up = False
r_paddle_down = False

ball_x = WINDOW_WIDTH / 2
ball_y = WINDOW_HEIGHT / 2
BALL_R = 10

ball_vx = 5
ball_vy = 5

game_in_progress = False

paddle_color = [1,1,1]
background_color = [0,0,0]
ball_color = [1,1,1]

def draw_paddles(r,g,b):
    set_fill_color(r,g,b)
    draw_rectangle(L_PADDLE_X, l_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(R_PADDLE_X, r_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

def draw_ball(r,g,b):
    set_fill_color(r,g,b)
    draw_circle(ball_x, ball_y, BALL_R)

def draw_background(r,g,b):
    set_clear_color(r,g,b)
    clear()

def draw_attributes():
    draw_background(background_color[0], background_color[1], background_color[2])
    draw_paddles(paddle_color[0], paddle_color[1], paddle_color[2])
    draw_ball(ball_color[0], ball_color[1], ball_color[2])

def update_ball():
    global ball_x, ball_y

    ball_x += ball_vx
    ball_y += ball_vy

def reset_game():
    global ball_x, ball_y, ball_vx, ball_vy, game_in_progress

    ball_x = WINDOW_WIDTH / 2
    ball_y = WINDOW_HEIGHT / 2
    ball_vx = 5
    ball_vy = 5

def update_paddles():
    global l_paddle_y, r_paddle_y

    if l_paddle_down and l_paddle_y > 0:
        l_paddle_y -= PADDLE_MOVEMENT_VALUE

    if l_paddle_up and l_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        l_paddle_y += PADDLE_MOVEMENT_VALUE

    if r_paddle_down and r_paddle_y > 0:
        r_paddle_y -= PADDLE_MOVEMENT_VALUE

    if r_paddle_up and r_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        r_paddle_y += PADDLE_MOVEMENT_VALUE

def ball_hit_paddle():
    return (ball_x - BALL_R <= PADDLE_WIDTH and ball_y in range(l_paddle_y, l_paddle_y + PADDLE_HEIGHT)) or (ball_x + BALL_R >= WINDOW_WIDTH - PADDLE_WIDTH and ball_y in range(r_paddle_y, r_paddle_y + PADDLE_HEIGHT))

def ball_hit_horizontal_boundary():
    return ball_y - BALL_R < 0 or ball_y + BALL_R > WINDOW_HEIGHT

def ball_out_of_bounds():
    return ball_x + BALL_R < 0 or ball_x - BALL_R > WINDOW_WIDTH


def keypress(key):
    global game_in_progress, l_paddle_up, l_paddle_down, r_paddle_up, r_paddle_down

    if key == " ": # pause
        game_in_progress = not game_in_progress

    elif key == "r": # reset
        reset_game()

    elif key == "z":
        l_paddle_up = True

    elif key == "a":
        l_paddle_down = True

    elif key== "m":
        r_paddle_up = True

    elif key == "k":
        r_paddle_down = True

def keyrelease(key):
    global l_paddle_up, l_paddle_down, r_paddle_up, r_paddle_down

    if key == "z":
        l_paddle_up = False

    elif key == "a":
        l_paddle_down = False

    elif key == "m":
        r_paddle_up = False

    elif key == "k":
        r_paddle_down = False


def draw():
    global ball_vx, ball_vy, game_in_progress

    draw_attributes()
    update_paddles()

    if game_in_progress:
        update_ball()

        if ball_hit_paddle():
            print("hit paddle")
            ball_vx *= -1

        if ball_hit_horizontal_boundary():
            print("hit ceiling")
            ball_vy *= -1

        if ball_out_of_bounds():
            print("out of bounds")
            game_in_progress = False
            reset_game()


start_graphics(draw, key_press=keypress, key_release=keyrelease, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=60)