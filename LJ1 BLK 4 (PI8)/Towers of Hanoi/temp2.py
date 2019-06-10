#In this built, 3 poles are being built and there are 8 disks total

import turtle

# Deceleration of global variables
screen_width_half = 600
screen_length_half = 350
pole_list = []
# Biggest to smallest
disk_list = []
# debug stuff delete after
main_window = turtle.Screen()
main_window.setup(1200, 700, None, None)
main_window.title("Kokosnoten zijn geen specerijen")


class PlayingField:

    def __init__(self):
        None


class PlayingFieldPole:

    def __init__(self):
        self.length = 140 + (8 * 20)
        # Default width is 20
        self.pole_content = []
        # Absolute coordinates in Screen
        self.x_pos = 0
        self.y_pos = 0

    def draw_self(self):
        # An "origin" is the point where the turtle starts drawing the image
        origin_x = self.x_pos
        origin_y = self.y_pos
        fill_color = "black"
        turtle_draw_a_box(self.length, 20, origin_x, origin_y, fill_color)


class TowerDisk:

    def __init__(self):
        # Calculated in create_disks
        self.width = 0
        # Default height is 20
        self.x_pos = 0
        self.y_pos = 0

    def draw_self(self):
        # An "origin" is the point where the turtle starts drawing the image
        origin_x = self.x_pos
        origin_y = self.y_pos
        fill_color = "Blue"
        turtle_draw_a_box(20, self.width, origin_x, origin_y, fill_color)

# Assuming origin is in the middle of the bottom line
def turtle_draw_a_box(length, width, x_pos, y_pos, fill_color):
    turtle.fillcolor(fill_color)
    turtle.setpos(x_pos, y_pos)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width / 2)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width / 2)
    turtle.end_fill()
    turtle.penup()


def create_poles():
    for i in range(3):
        # Creates the poles in memory
        pole_list.append(PlayingFieldPole())
        pole_list[i].x_pos = -310 + (300 * i)
        pole_list[i].y_pos = -150
        #Draws the poles
        pole_list[i].draw_self()


def create_disks():

    for i in range(8):
        # Creates disks in memory
        disk_list.append(TowerDisk((200 * (1 - (i * 0.1))), -310, (-150 + (20 * i))))
        # disk_list[i].width = 200 * (1 - (i * 0.1))
        # disk_list[i].x_pos = -310
        #20 = height
        # disk_list[i].y_pos = -150 + (20 * i)
        disk_list[i].draw_self()
    pole_list[0].pole_content = disk_list


# Code excecution starts here

turtle.penup()
create_poles()
create_disks()
print(pole_list[0].pole_content)
print(disk_list)
# This makes sure the program doesn't quit on its own
turtle.mainloop()
