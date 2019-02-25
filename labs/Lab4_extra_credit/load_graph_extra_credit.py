# Author: Thomas Monfre
# Date: 11/8/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines a function that read lines from a text file, creating a Vertex object for each line. It
#          also stores each object in a dictionary, then adds the objects of the adjacent vertices of each vertex into
#          an instance variable list of said object.

# import class Vertex
from vertex_extra_credit import Vertex

# given a key, return the key's value in the dictionary
def find_dictionary_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None

# goes through file creating Vertex objects and storing them in dictionary
def load_graph(file_name):
    # open file to be read
    in_file = open(file_name, "r")

    # create new dictionary
    dictionary = {}

    # sweep through the file, creating a new Vertex object with its name and x,y location
    for line in in_file:
        # split line up into elements of list every time a semi-colon is encountered
        line = line.split(";")

        # split the element for x and y location into its own list to separate out values
        x_y = line[2].split(",")

        # create local variables for the name of the vertex as well as its x,y location
        name = line[0]
        x = x_y[0]
        y = x_y[1]

        # create new_object and add it to the dictionary
        new_object = Vertex(name,x,y)
        dictionary[name] = new_object

    # close the file and immediately re-open it
    in_file.close()
    in_file = open(file_name, "r")

    # sweep through the file a second time to add adjacent Vertex objects to adjacent_list instance variable of object
    for line in in_file:
        # split line up into elements of list every time a semi-colon is encountered
        line = line.split(";")

        # create local variables for the name of the vertex as well as its adjacent vertices (list)
        name = line[0]
        adj_vertices = line[1]

        # split the string of vertices into a list every time a comma is encountered
        adj_vertices = adj_vertices.split(",")

        # vertex currently being looked at
        current_vertex = find_dictionary_value(dictionary, name)

        # for each vertex that is adjacent to the current one, find its value in the dictionary and append it to the
        # current vertex's list of vertices adjacent to it
        for vertex in adj_vertices:
            vertex = vertex.strip()
            new_vertex = find_dictionary_value(dictionary, vertex)
            current_vertex.adj_list.append(new_vertex)

    return dictionary