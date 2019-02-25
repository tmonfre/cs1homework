# Author: Thomas Monfre
# Date: 10/24/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program is the test code for the Body and System classes. It draws the Sun in the center of the screen
#          with the first four planets of the solar system orbiting around it.

from cs1lib import *
from system_extra_credit import System
from body_extra_credit import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 2000000 # real seconds per simulation second
PIXELS_PER_METER = 120. / 149.6e9 # distance scale for the simulation (fraction of Earth's distance from sun)

FRAMERATE = 30 # frames per second
TIMESTEP = 1.0 / FRAMERATE # time between drawing each frame

# create the bodies in the System by making them objects of the Body class
sun = Body(1.98892e30, 0, 0, 0, 0, 10, load_image("sun.png"))
mercury = Body(0.330e24, 57.9e9, 0, 0, 47.4e3, 3, load_image("mercury.png"))
venus = Body(4.87e24, 108.2e9, 0, 0, 35.0e3, 5, load_image("venus.png"))
earth = Body(5.97e24, 149.6e9, 0, 0, 29.8e3, 6, load_image("earth.png"))
mars = Body(0.642e24, 227.9e9, 0, 0, 24.1e3, 4, load_image("mars.png"))

# create the system by creating a list of the bodies and making that list an object of the System class
solar_system = System([sun, mercury, venus, earth, mars])

# draw the system
def main():
    # make background image of stars
    clear()
    background = load_image("background.png")
    draw_image(background, 0, 0)

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

start_graphics(main, 2400, framerate=FRAMERATE)