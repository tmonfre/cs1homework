# Author: Thomas Monfre
# Date: 11/8/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program draws a graph over a map of Dartmouth College and computes the fastest path a user can travel
#          to get from one point to another (based on where they click on the map)

from cs1lib import *
from load_graph_extra_credit import load_graph
from queue_extra_credit import Queue

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

# radius of the circle that will represent a radius on the map
VERTEX_RADIUS = 10

# load the map image for the background and create a dictionary of vertex names and their respective objects
background_image = load_image("dartmouth_map.png")
dictionary = load_graph("dartmouth_graph.txt")

# create lists for basic colors used throughout the program
red = [1,0,0]
blue = [0,0.3,1]

# set three major global variables that structure the program - used to determine how the graph is drawn on the map
start_vertex_selected = False
start_vertex = None
goal_vertex = None

# returns a path of vertices that connect the start and goal vertices over the smallest possible distance
def breadth_first_search(start,goal):
    # create a queue and enqueue the start vertex
    queue = Queue()
    queue.enqueue(start)

    # create a dictionary of backpointers
    bp_dictionary = {}

    # define the distance from the start vertex of each vertex to infinity
    for vertex in dictionary:
        dictionary[vertex].distance_from_start = float('inf')

    # define the distance from the start vertex to the start vertex to 0 and set its backpointer as None
    dictionary[start].distance_from_start = 0
    bp_dictionary[start] = None

    # loop through the queue, checking each element's adjacency list for vertices that haven't been visited
    # and storing their distance from the starting vertex
    while goal not in bp_dictionary:
        if not queue.is_empty():
            search = queue.dequeue()

            for vertex in dictionary[search].adj_list:
                vertex_name = vertex.name

                if vertex_name not in bp_dictionary:
                    dictionary[vertex_name].distance_from_start = dictionary[search].distance_from_start + 1
                    bp_dictionary[vertex_name] = search
                    queue.enqueue(vertex_name)

    # create path to be returned for how to get to start from goal (following backpointers)
    path = []
    # set last visited vertex along path as the goal
    last = goal

    # follow each vertex by its backpointers, adding them to the list until start is found
    while last != start:
        path.append(last)
        last = bp_dictionary[last]

    return path

# call breadth_first_search to return a path of connected vertices, then draw the vertices and edges along that path red
def draw_path(start,goal):
    path = breadth_first_search(start,goal)

    # draws the vertices and edges along the path red
    for index in range(len(path)):
        # draw vertex
        dictionary[path[index]].draw_vertex(red[0], red[1], red[2])

        # draw edge between current vertex and next vertex
        if index < len(path) - 1:
            dictionary[path[index]].draw_edge(dictionary[path[index + 1]], red[0], red[1], red[2])

        # draw vertex from start back to next vertex (opposite direction)
        dictionary[start].draw_edge(dictionary[path[len(path) - 1]], red[0], red[1], red[2])

# function called by start_graphics to draw the map and graph
def draw():
    draw_image(background_image, 0, 0)

    # draw all the vertices and edges blue
    for key in dictionary:
        dictionary[key].draw_all_edges(blue[0], blue[1], blue[2])
        dictionary[key].draw_vertex(blue[0], blue[1], blue[2])

    # if a start vertex and goal_vertex are selected by the user, draw the path connected those vertices red
    if start_vertex != None and goal_vertex != None:
        draw_path(start_vertex, goal_vertex)

    # if a start_vertex is selected, draw its vertex red and print its name
    if start_vertex != None:
        dictionary[start_vertex].draw_vertex(red[0], red[1], red[2])
        dictionary[start_vertex].draw_name()

    # if a goal_vertex is selected, draw its vertex red and print its name
    if goal_vertex != None:
        dictionary[goal_vertex].draw_vertex(red[0], red[1], red[2])
        dictionary[goal_vertex].draw_name()

# if the user clicks on a vertex, set that vertex as the start_vertex
def mousepress(mx,my):
    global start_vertex_selected, start_vertex

    # loop through dictionary to figure out which vertex the user clicked on
    for key in dictionary:
        x_range = dictionary[key].x
        y_range = dictionary[key].y

        if mx in range(x_range - VERTEX_RADIUS, x_range + VERTEX_RADIUS + 1) and my in range(y_range - VERTEX_RADIUS, y_range + VERTEX_RADIUS + 1):
            start_vertex = dictionary[key].name
            start_vertex_selected = True

# if the user moves the mouse after selecting a vertex, set the goal_vertex to whatever vertex the mouse is over
def mousemove(mx,my):
    global goal_vertex

    # if the user clicked on a start_vertex, figure out which vertex the mouse is over and set that to the goal_vertex
    if start_vertex_selected:
        for key in dictionary:
            x_range = dictionary[key].x
            y_range = dictionary[key].y

            if mx in range(x_range - VERTEX_RADIUS, x_range + VERTEX_RADIUS + 1) and my in range(y_range - VERTEX_RADIUS, y_range + VERTEX_RADIUS + 1):
                goal_vertex = dictionary[key].name

# if the user presses space, clear the map of any selected start vertices, goal vertices, or path
# if the user presses "q" quit the program
def keypress(key):
    global start_vertex, goal_vertex, start_vertex_selected
    if key == "q":
        cs1_quit()

    if key ==" ":
        start_vertex = None
        goal_vertex = None
        start_vertex_selected = False

# open a graphics window with this program
start_graphics(draw, mouse_press=mousepress, mouse_move=mousemove, key_press=keypress, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title="Map of Dartmouth")