# Author: Thomas Monfre
# Date: 10/24/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class Body that, given characteristics of a celestial body, creates an object that
#          represents a celestial body, then updates the position and velocity of that body in time.

from cs1lib import *

class Body:
    # instance variables this class receives
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        # physical properties of object
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        # values used to draw object
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # updates the position of the object based on its velocity in x, y directions and the timestep
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    # updates the velocity of the object based on its acceleration in x, y directions and the timestep
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    # draws the object in coordinate system
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        disable_stroke()

        location_x = cx + self.x * pixels_per_meter
        location_y = cy + self.y * pixels_per_meter

        draw_circle(location_x, location_y, self.pixel_radius)

    # string method used to determine where each object is located
    def __str__(self):
        return "The body is at position " + str(self.x) + "," + str(self.y)