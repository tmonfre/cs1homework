from crowd import Crowd
from cs1lib import *

crowd = Crowd(1000)

def draw():
    clear()
    crowd.draw()

def keypress(key):
     if key == " ":
         crowd.remove_overlapping()

start_graphics(draw, key_press=keypress)