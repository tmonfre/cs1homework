# Author: Thomas Monfre
# Date: 11/1/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program will sort information in cities_out.txt using the quicksort function

from city import City
from quicksort import sort

# given a list and a file to write to, loop through the list of objects and call the __str__ method of each object,
# writing that line into the file. Range is used so a new line won't be created when the loop is on the last line
def write_to_file(list, file_name):
    for i in range(len(list)):
        # if this is the last element to be printed, simply print the line and don't create a new one
        if i == len(list) - 1:
            file_name.write(str(list[i]))
        # if there are more elements to be printed, print the line then start a new line
        else:
            string = str(list[i]) + "\n"
            file_name.write(string)

# sorting method for comparing city names alphabetically
def compare_city_names(city1, city2):
    return city1.name.lower() <= city2.name.lower()

# sorting method for comparing city populations greatest to least
def compare_city_populations(city1, city2):
    return city1.population >= city2.population

# sorting method for comparing city populations greatest to least
def compare_city_latitudes(city1, city2):
    return city1.latitude <= city2.latitude

# open original file of cities to be read
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

# close original file of cities and open new file to be written to alphabetically based on city name
cities_in.close()
cities_alpha = open("cities_alpha.txt", "w")

# sort the list of city objects alphabetically based on name, then write each line of that list to cities_alpha
sort(list_objects, compare_city_names)
write_to_file(list_objects, cities_alpha)

# close the file sorted by city name and open new file to be written to numerically based on population
cities_alpha.close()
cities_population = open("cities_population.txt", "w")

# sort the list of city objects numerically based on population, then write each line of that list to cities_population
sort(list_objects, compare_city_populations)
write_to_file(list_objects, cities_population)

# close the file sorted by city name and open new file to be written to numerically based on population
cities_population.close()
cities_latitude = open("cities_latitude.txt", "w")

# sort the list of city objects numerically based on population, then write each line of that list to cities_population
sort(list_objects, compare_city_latitudes)
write_to_file(list_objects, cities_latitude)

# close the file sorted by city latitude
cities_latitude.close()