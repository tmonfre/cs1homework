# Author: Thomas Monfre
# Date: 10/21/17
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

    # updates the position of both objects - also calculates the acceleration of the moon in x & y directions via a
    # given total acceleration and passes that to the update_velocity method from the Body class

    # in this example, only the velocity of the moon is updated and it is passed a set acceleration from the problem
    # description. In the final version, there will be an additional method in this class to calculate the acceleration
    # for all objects based on mass, distance, and the gravitational constant G.
    def update(self, timestep):

        # calculate distance of the bodies from each other in x and y directions, then compute the radius from that
        dx = self.body_list[0].x - self.body_list[1].x
        dy = self.body_list[0].y - self.body_list[1].y
        r = sqrt(dx * dx + dy * dy)

        # split acceleration into x and y directions. 0.0028 is the value given from the project description
        ax = 0.0028 * dx / r
        ay = 0.0028 * dy / r

        # update position
        for i in range(len(self.body_list)):
            self.body_list[i].update_position(timestep)

        # update velocity
        self.body_list[1].update_velocity(ax, ay, timestep)