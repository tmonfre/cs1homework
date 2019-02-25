# Author: Thomas Monfre
# Date: 10/30/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program reads the file world_cities.txt making each line an object of class City, then writing a new
#          text file cities_out.txt in which each line is the object of the City class' __str__ method

from city import City

# open file to be read
cities_in = open("world_cities.txt", "r")

# create list that objects of the class City will be appended to
list_objects = []

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

# close old file and open new one to be written to 
cities_in.close()
cities_out = open("cities_out.txt", "w")

# loop through the list of objects and call the __str__ method of each object, writing that line into the new file
# range is used so a new line won't be created when the loop is on the last line
for i in range(len(list_objects)):
    # if this is the last element to be printed, simply print the line and don't create a new one
    if i == len(list_objects) - 1:
        cities_out.write(str(list_objects[i]))
    # if there are more elements to be printed, print the line then start a new line
    else:
        string = str(list_objects[i]) + "\n"
        cities_out.write(string)