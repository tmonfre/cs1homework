# Author: Thomas Monfre
# Date: 10/24/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class Body that, given characteristics of a celestial body, creates an object that
#          represents a celestial body, then updates the position and velocity of that body in time.

from cs1lib import *

class Body:
    # instance variables this class receives
    def __init__(self, mass, x, y, vx, vy, pixel_radius, file_name):
        # physical properties of object
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        # values used to draw object - the pixel_radius is used to center the image and the file name corresponds to
        # a .png image of the planet
        self.pixel_radius = pixel_radius
        self.file_name = file_name

    # updates the position of the object based on its velocity in x, y directions and the timestep.
    # this method also makes the updated position more accurate by subdividing the timestep, calculating new
    # positions with that smaller timestep, and accumulating them.
    def update_position(self, timestep, subdivide):
        new_timestep = timestep / subdivide

        for i in range(subdivide):
            self.x = self.x + self.vx * new_timestep
            self.y = self.y + self.vy * new_timestep

    # updates the velocity of the object based on its acceleration in x, y directions and the timestep.
    # this method also makes the updated velocities more accurate by subdividing the timestep, calculating new
    # velocities with that smaller timestep, and accumulating them.
    def update_velocity(self, ax, ay, timestep, subdivide):
        new_timestep = timestep / subdivide

        for i in range(subdivide):
            self.vx = self.vx + ax * new_timestep
            self.vy = self.vy + ay * new_timestep

    # draws the object in coordinate system by loading an image of the Body and centering it
    def draw(self, cx, cy, pixels_per_meter):

        location_x = cx + self.x * pixels_per_meter
        location_y = cy + self.y * pixels_per_meter

        # centers the image in its proper location by setting the x and y locations to the top left corner of image
        draw_image(self.file_name, location_x - self.pixel_radius, location_y - self.pixel_radius)

    # string method used to determine where each object is located
    def __str__(self):
        return "The body is at position " + str(self.x) + "," + str(self.y)