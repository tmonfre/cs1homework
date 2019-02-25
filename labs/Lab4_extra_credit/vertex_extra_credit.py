# Author: Thomas Monfre
# Date: 11/8/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines the class Vertex that creates objects for vertices of a graph overlaying a map of
#          Dartmouth College.

from cs1lib import *

VERTEX_RADIUS = 7
EDGE_WIDTH = 4

class Vertex:
    # receive instance variable for name and x,y location. List of adjacent vertices starts empty, will be appended to
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = []
        self.distance_from_start = None

    # draw circle for vertex on map
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)

        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # draw edges between two vertices
    def draw_edge(self, object, r, g, b):
        enable_stroke()
        set_stroke_width(EDGE_WIDTH)
        set_stroke_color(r, g, b)

        draw_line(self.x, self.y, object.x, object.y)

    # draw edges between self vertex and all adjacent vertices
    def draw_all_edges(self, r, g, b):
        for object in self.adj_list:
            object.draw_edge(self, r, g, b)

    # draw the name of the selected vertex on the screen above the circle representing the vertex
    def draw_name(self):
        enable_stroke()
        set_font_size(17)
        set_font_bold()
        set_stroke_color(0,0,0)

        length = len(self.name)

        x = self.x - 0.6 * length * VERTEX_RADIUS
        y = self.y - 2 * VERTEX_RADIUS

        draw_text(self.name, x, y)

    # returns information about each vertex to be printed
    def __str__(self):
        # concatenate the names of the Vertex objects in the adjacency list to an empty string
        adj_string = ""
        for index in range(len(self.adj_list)):
            # no comma after name
            if index == len(self.adj_list) - 1:
                adj_string = adj_string + str(self.adj_list[index].name)
            # comma after name
            else:
                adj_string = adj_string + str(self.adj_list[index].name) + ", "

        # final string to be printed
        return str(self.name) + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent Vertices: " + str(adj_string)