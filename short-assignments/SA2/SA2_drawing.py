# Author: Thomas Monfre
# Date: 9/16/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program is designed to recreate the cover to the children's book "The Very Hungry Caterpillar"

from cs1lib import *

# the following functions will define fill, background, and stroke colors
def set_fill_red():
    set_fill_color(0.9, 0, 0)

def set_fill_white():
    set_fill_color(1, 1, 1)

def set_fill_yellow():
    set_fill_color(1, 1, 0)

def set_fill_green():
    set_fill_color(0, 0.6, 0)

def set_fill_blue():
    set_fill_color(0.25, 0, 0.5)

def set_stroke_black():
    set_stroke_color(0, 0, 0)

def set_stroke_red():
    set_stroke_color(0.9, 0, 0)

def set_stroke_blue():
    set_stroke_color(0.25, 0, 0.5)

def make_background_pale_blue():
    set_clear_color(0.94, 0.94, 1)
    clear()

# the following functions and variables will be used to draw the head of the caterpillar
head_center_x = 300
head_center_y = 250

def draw_head_shape():
    set_fill_red()
    set_stroke_black()
    draw_ellipse(head_center_x, head_center_y, 35, 45)

def draw_inside_left_eye():
    set_fill_green()
    draw_ellipse(head_center_x - 10, head_center_y - 9, 5, 7)

def draw_inside_right_eye():
    set_fill_green()
    draw_ellipse(head_center_x + 10, head_center_y - 9, 5, 7)

def draw_outside_left_eye():
    set_fill_yellow()
    draw_ellipse(head_center_x - 10, head_center_y - 9, 10, 13)

def draw_outside_right_eye():
    set_fill_yellow()
    draw_ellipse(head_center_x + 10, head_center_y - 9, 10, 13)

def draw_mouth():
    set_fill_red()
    set_stroke_black()
    draw_ellipse(head_center_x, head_center_y + 15, 13, 8)

def cover_mouth():
    set_fill_red()
    set_stroke_red()
    draw_rectangle(head_center_x - 15, head_center_y + 5, 30, 10)

def draw_left_antenna():
    set_fill_blue()
    set_stroke_blue()
    draw_ellipse(head_center_x - 8, head_center_y - 50, 3, 14)

def draw_right_antenna():
    set_fill_blue()
    set_stroke_blue()
    draw_ellipse(head_center_x + 8, head_center_y - 50, 3, 14)

def draw_head():
    draw_left_antenna()
    draw_right_antenna()
    draw_head_shape()
    draw_outside_left_eye()
    draw_outside_right_eye()
    draw_inside_left_eye()
    draw_inside_right_eye()
    draw_mouth()
    cover_mouth()

# the following functions will draw the body of the caterpillar, segments are ordered right to left
def body_attributes(): # defines basic color attributes of caterpillar body
    set_fill_green()
    set_stroke_black()

def draw_first_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 25, head_center_y - 5, 40, 45)

def draw_second_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 50, head_center_y - 20, 40, 45)

def draw_third_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 65, head_center_y - 30, 40, 45)

def draw_fourth_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 90, head_center_y - 45, 40, 45)

def draw_fifth_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 110, head_center_y - 48, 40, 45)

def draw_sixth_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 130, head_center_y - 45, 40, 45)

def draw_seventh_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 150, head_center_y - 35, 40, 45)

def draw_eighth_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 170, head_center_y - 25, 40, 45)

def draw_ninth_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 190, head_center_y - 10, 40, 45)

def draw_tenth_body_segment():
    body_attributes()
    draw_ellipse(head_center_x - 205, head_center_y - 5, 40, 45)

def draw_body():
    draw_tenth_body_segment()
    draw_ninth_body_segment()
    draw_eighth_body_segment()
    draw_seventh_body_segment()
    draw_sixth_body_segment()
    draw_fifth_body_segment()
    draw_fourth_body_segment()
    draw_third_body_segment()
    draw_second_body_segment()
    draw_first_body_segment()

# the following functions will draw the legs of the caterpillar, legs are numbered right to left
def draw_leg_one():
    set_stroke_black()
    draw_line(head_center_x + 10, head_center_y + 43, head_center_x + 10, head_center_y + 55) # vertical leg
    draw_line(head_center_x + 10, head_center_y + 55, head_center_x + 15, head_center_y + 55) # horizontal foot

def draw_leg_two():
    set_stroke_black()
    draw_line(head_center_x - 10, head_center_y + 43, head_center_x - 10, head_center_y + 55) # vertical leg
    draw_line(head_center_x - 10, head_center_y + 55, head_center_x - 5, head_center_y + 55) # horizontal foot

def draw_leg_three():
    set_stroke_black()
    draw_line(head_center_x - 223, head_center_y + 36, head_center_x - 223, head_center_y + 50) # vertical leg
    draw_line(head_center_x - 223, head_center_y + 50, head_center_x - 218, head_center_y + 50) # horizontal foot

def draw_leg_four():
    set_stroke_black()
    draw_line(head_center_x - 200, head_center_y + 40, head_center_x - 200, head_center_y + 50) # vertical leg
    draw_line(head_center_x - 200, head_center_y + 50, head_center_x - 195, head_center_y + 50) # horizontal foot

def draw_legs():
    draw_leg_one()
    draw_leg_two()
    draw_leg_three()
    draw_leg_four()

def draw_caterpillar(): # puts all components of caterpillar together
    draw_body()
    draw_head()
    draw_legs()

# the following functions will draw the text
def draw_title():
    set_font_bold()
    set_font_size(35)
    draw_text("The Very Hungry", 60, 70)
    draw_text("Caterpillar", 110, 110)

def draw_name():
    set_font_size(15)
    set_font_bold()
    draw_text("Thomas Monfre", 20, 380)

# final function used to put all the pieces of the book cover together
def draw_book_cover():
    make_background_pale_blue()
    draw_caterpillar()
    draw_title()
    draw_name()

start_graphics(draw_book_cover, title="The Very Hungry Caterpillar")