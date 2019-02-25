# Author: Thomas Monfre
# Date: 10/30/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program visualizes data of the city class to represent the top 50 most populous cities in the world

from cs1lib import *
from city import City
from quicksort import sort
from random import randint, uniform

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

# number of cities to be drawn on the map
NUM_CITIES = 50

# sorting method for comparing city populations greatest to least
def compare_city_populations(city1, city2):
    return city1.population >= city2.population

# background image of the map
background = load_image("world.png")

# load list of world cities and create empty list to store them in
cities_in = open("world_cities.txt", "r")
list_objects = []

# create an object for each city in the file and store in list_objects
for line in cities_in:
    # strip away the whitespace from the beginning and end of each line
    line.strip()
    # separate each line (originally one string) into several strings within a list every time a comma is found
    list_for_class = line.split(",")

    # assign temporary variables to be used as instance variables for each object of the class City
    country_code = list_for_class[0]
    city_name = list_for_class[1]
    region = list_for_class[2]
    population = str(list_for_class[3])
    latitude = str(list_for_class[4])
    longitude = str(list_for_class[5])

    # create an object of the class City then append it to the list of objects
    city = City(country_code, city_name, region, population, latitude, longitude)
    list_objects.append(city)

# sort the list by population
sort(list_objects, compare_city_populations)


# draw the background map image as well as the boxes, and update their positions as necessary
def draw():
    clear()
    draw_image(background, 0, 0)

    for i in range(NUM_CITIES + 1):
        list_objects[i].draw_box()
        list_objects[i].update()


# reset the boxes to a random location and color if user presses space, quit program if user presses 'q'
def keypress(key):
    if key == " ":
        for i in range(NUM_CITIES + 1):
            list_objects[i].x = randint(20, 720)
            list_objects[i].y = randint(20, 340)

            list_objects[i].r = uniform(0, 1)
            list_objects[i].g = uniform(0, 1)
            list_objects[i].b = uniform(0, 1)

    if key == "q":
        cs1_quit()

# if the user clicks on the box representing the city, print the name and population of the city to the console
def mousepress(mx,my):
    for i in range(NUM_CITIES + 1):
        if mx in range(int(list_objects[i].x) - 4, int(list_objects[i].x) + 4) and my in range(int(list_objects[i].y) - 4, int(list_objects[i].y) + 4):
            # change the color of the box red so the user knows they clicked on it
            list_objects[i].r = 1
            list_objects[i].g = 0
            list_objects[i].b = 0

            print()
            print(str(list_objects[i].name) + ": Population " + str(list_objects[i].population))
            print(str(list_objects[i].name) + " is the #" + str(i + 1) + " most populous city in the world.")

start_graphics(draw, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, key_press=keypress, mouse_press=mousepress, framerate=60)