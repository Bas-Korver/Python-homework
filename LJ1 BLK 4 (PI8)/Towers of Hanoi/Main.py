import tkinter
import sys
import turtle


class GameStartWindow:
    def __init__(self, master):
        self.master = master
        x_coordinate = int((master.winfo_screenwidth() / 2) - 127)
        y_coordinate = int((master.winfo_screenheight() / 2) - 60)
        master.geometry("254x120+{}+{}".format(x_coordinate, y_coordinate))
        master.title('Towers of Hanoi')

        self.levels = [6, 8]
        self.label_one = tkinter.Label(master,
                                       text='Choose Level, 6 = six rings and '
                                            '8 = eight rings')
        self.label_one.place(x=4, y=10)
        self.variable = tkinter.StringVar(master)
        self.variable.set("6")
        self.user_entry = tkinter.OptionMenu(master, self.variable,
                                             *self.levels)
        self.user_entry.place(x=90, y=35)
        self.submit_button = tkinter.Button(master, text='Submit',
                                            command=self.action, height=1,
                                            width=10)
        self.submit_button.place(x=10, y=85)
        self.exit_button = tkinter.Button(master, text='Exit',
                                          command=sys.exit,
                                          height=1, width=10)
        self.exit_button.place(x=164, y=85)
        master.bind('<Return>', self.action)

    def action(self, event = None):
        self.master.destroy()
        self.a = self.variable.get()


class GameEndWindow:
    def __init__(self, master):
        self.master = master
        x_coordinate = int((master.winfo_screenwidth() / 2) - 127)
        y_coordinate = int((master.winfo_screenheight() / 2) - 60)
        master.geometry("254x120+{}+{}".format(x_coordinate, y_coordinate))
        master.title('Towers of Hanoi')

        self.label_one = tkinter.Label(master,
                                       text='You won!')
        self.label_one.place(x=4, y=10)
        self.submit_button = tkinter.Button(master, text='Restart',
                                            command=self.action, height=1,
                                            width=10)
        self.submit_button.place(x=10, y=85)
        self.exit_button = tkinter.Button(master, text='Exit',
                                          command=sys.exit,
                                          height=1, width=10)
        self.exit_button.place(x=164, y=85)
        master.bind('<Return>', self.action)

    def action(self, event=None):
        self.master.destroy()
        root = tkinter.Tk()
        my_gui = GameStartWindow(root)
        root.mainloop()
        print(my_gui.a)





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
        disk_list.append(TowerDisk())
        disk_list[i].width = 200 * (1 - (i * 0.1))
        disk_list[i].x_pos = -310
        #20 = height
        disk_list[i].y_pos = -150 + (20 * i)
        disk_list[i].draw_self()
    pole_list[0].pole_content = disk_list

root = tkinter.Tk()
my_gui = GameStartWindow(root)
root.mainloop()
print(my_gui.a)


# Code excecution starts here

turtle.penup()
create_poles()
create_disks()
print(pole_list[0].pole_content)
print(disk_list)
# This makes sure the program doesn't quit on its own
turtle.mainloop()