# Author: Thomas Monfre
# Date: 10/30/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class City that stores information about various cities in objects of this class.
#          Additionally, this class has methods to draw boxes representing each city and animate them. The animation
#          starts the location of the box at a random spot on the map, then updates its location until it reaches its
#          final destination.

from cs1lib import *
from random import randint, uniform

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

# pixel conversion for degrees of latitude or longitude
PIXELS_PER_LONG = WINDOW_WIDTH / (WINDOW_WIDTH / 2)
PIXELS_PER_LAT = WINDOW_HEIGHT / (WINDOW_HEIGHT / 2)

BOX_DIAMETER = 7.5

class City:
    # class City takes six instance variables in addition to self
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

        # initially set the location of the box randomly
        self.x = randint(20, 720)
        self.y = randint(20, 340)

        # calculate the final position where the box should be (where the city is on the map)
        self.final_x = (WINDOW_WIDTH / 2) + self.longitude * PIXELS_PER_LONG
        self.final_y = (WINDOW_HEIGHT / 2) - self.latitude * PIXELS_PER_LAT

        # set random values for the color of the box that represents each city
        self.r = uniform(0,1)
        self.g = uniform(0,1)
        self.b = uniform(0,1)

    # draw a box representing each object as a city on a map
    def draw_box(self):
        set_fill_color(self.r, self.g, self.b)
        disable_stroke()

        # 0.5 * BOX_DIAMETER represents the radius -- by subtracting the box is centered on its x,y coordinates
        draw_rectangle(self.x - (0.5 * BOX_DIAMETER), self.y - (0.5 * BOX_DIAMETER), BOX_DIAMETER, BOX_DIAMETER)

    # update location of box if it is not in its final place
    def update(self):
        # if the box is a reasonable distance away from its final location, move it closer to its final spot
        if self.final_x - self.x > 10 and self.final_y - self.y > 10:
            self.x = self.x + ((self.final_x - self.x) / 20)
            self.y = self.y + ((self.final_y - self.y) / 20)
        # if the box is not at its final location but close, move it closer but by a greater margin.
        # this is done to avoid the program taking a long period of time to adjust the final location as the
        # distance between final location and current location gets smaller and smaller.
        elif self.x != self.final_x and self.y != self.final_y:
            self.x = self.x + ((self.final_x - self.x) / 8)
            self.y = self.y + ((self.final_y - self.y) / 8)

    # returns the name, population, latitude, and longitude of each object in a string to be printed
    def __str__(self):
        return str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)