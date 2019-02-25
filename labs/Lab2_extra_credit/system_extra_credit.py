# Author: Thomas Monfre
# Date: 10/24/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class System that, given a list of Body objects, creates a System of objects
#          and updates their values as such.

from math import sqrt

G = 6.67384e-11

class System:
    # this class receives one instance variable, the list of Body objects
    def __init__(self, body_list):
        self.body_list = body_list

    # draws the system of bodies by calling the method draw from the Body class
    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)

    # updates the position and velocity of all objects in the system
    # velocity is updated by computing the acceleration of each body due to the other bodies in the system
    # this method allows for a more accurate system by subdividing the timestep, and accumulating the new velocities
    # and positions based on the smaller timestep
    def update(self, timestep):
        for i in range(len(self.body_list)):
            (ax,ay) = self.compute_acceleration(i)

            subdivide = 100

            self.body_list[i].update_velocity(ax, ay, timestep, subdivide)
            self.body_list[i].update_position(timestep, subdivide)

    # calculates the acceleration in the x and y directions for each Body in the System (called by update method)
    def compute_acceleration(self, index):
        ax = 0
        ay = 0
        for i in range(len(self.body_list)):
            # ensures that it does not attempt to calculate the acceleration due to itself (Python would return a float
            # division by zero error if so)
            if i != index:
                dx = self.body_list[i].x - self.body_list[index].x
                dy = self.body_list[i].y - self.body_list[index].y

                r = sqrt(dx * dx + dy * dy)

                acceleration = (G * self.body_list[i].mass) / (r * r)

                ax = ax + ((acceleration * dx) / r)
                ay = ay + ((acceleration * dy) / r)

        return ax, ay