# Author: Thomas Monfre
# Date: 10/21/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program is the test code for the Body and System classes. It draws Earth in the center of the screen
#          with the moon orbiting around it.

from cs1lib import *
from system_extra_credit import System
from body_extra_credit import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # real seconds per simulation second
PIXELS_PER_METER = 3 / 1e7  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    earth_moon.update(TIMESTEP * TIME_SCALE)

earth = Body(5.9736e24, 0, 0, 0, 0, 24, load_image("earth.png"))            # blue earth
moon = Body(7.3477e22, 3.84403e8, 0, 0, 1022, 4, load_image("venus.png"))   # white moon
earth_moon = System([earth, moon])  # list of bodies that are an object of the System class

start_graphics(main, 2400, framerate=FRAMERATE)