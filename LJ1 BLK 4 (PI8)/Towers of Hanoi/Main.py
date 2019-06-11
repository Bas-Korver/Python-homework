import tkinter
import turtle
import time
import sys
import os

class GameStartWindow:
    def __init__(self, master):
        self.master = master
        x_coordinate = int((master.winfo_screenwidth() / 2) - 127)
        y_coordinate = int((master.winfo_screenheight() / 2) - 60)
        master.geometry("254x120+{}+{}".format(x_coordinate, y_coordinate))
        master.title('Towers of Hanoi')

        self.levels = [3, 4, 5, 6, 7, 8, 9]
        self.label_one = tkinter.Label(master,
                                       text='Choose your Level. Level 3 '
                                            'being three rings, etc')
        self.label_one.place(x=4, y=10)
        self.variable = tkinter.StringVar(master)
        self.variable.set(3)
        self.user_entry = tkinter.OptionMenu(master, self.variable,
                                             *self.levels)
        self.user_entry.place(x=90, y=35)
        self.submit_button = tkinter.Button(master, text='Submit',
                                            command=self.submit_function,
                                            height=1,
                                            width=10)
        self.submit_button.place(x=10, y=85)
        self.exit_button = tkinter.Button(master, text='Exit',
                                          command=exit,
                                          height=1, width=10)
        self.exit_button.place(x=164, y=85)
        master.bind('<Return>', self.submit_function)

    def submit_function(self, event=None):
        self.master.destroy()
        self.chosen_level = self.variable.get()


class GameEndWindow:
    def __init__(self, master, moves_made, start_time):
        self.master = master
        self.moves_made = moves_made
        self.elapsed_time = round(((time.time() - start_time) / 60), 2)
        x_coordinate = int((master.winfo_screenwidth() / 2) - 127)
        y_coordinate = int((master.winfo_screenheight() / 2) - 60)
        master.geometry("254x120+{}+{}".format(x_coordinate, y_coordinate))
        master.title('Towers of Hanoi')

        self.label_one = tkinter.Label(master,
                                       text='You won!')
        self.label_one.place(x=4, y=10)
        self.variable_one = tkinter.StringVar(master)
        self.variable_one.set('You have made {} moves '.format(self.moves_made))
        self.label_two = tkinter.Label(master, textvariable=self.variable_one)
        self.label_two.place(x=4, y=35)
        self.variable_two = tkinter.StringVar(master)
        self.variable_two.set('and you have taken {} minute(s)'.format(self.elapsed_time))
        self.label_three = tkinter.Label(master, textvariable=self.variable_two)
        self.label_three.place(x=4, y=50)
        self.restart_button = tkinter.Button(master, text='Restart',
                                             command=self.restart_function,
                                             height=1,
                                             width=10)
        self.restart_button.place(x=10, y=85)
        self.exit_button = tkinter.Button(master, text='Exit',
                                          command=exit,
                                          height=1, width=10)
        self.exit_button.place(x=164, y=85)
        master.bind('<Return>', self.restart_function)

    def restart_function(self, event=None):
        self.master.destroy()



class DiskMoveHelper:

    def __init__(self):
        # Tower which the disks is being moved from
        self.origin_tower = False
        self.destination_tower = False
        self.button_pressed = False

    def button_zero(self, x, y):
        print("kms")
        self.button_pressed = 0
        self.select_destination_origin()

    def button_one(self, x, y):
        print("mks")
        self.button_pressed = 1
        self.select_destination_origin()

    def button_two(self, x, y):
        self.button_pressed = 2
        self.select_destination_origin()

    def select_destination_origin(self):
        if self.origin_tower == False:
            self.origin_tower = pole_list[self.button_pressed]
            print(self.origin_tower)
        else:
            self.destination_tower = pole_list[self.button_pressed]
            print(self.destination_tower)
            if self.origin_tower != self.destination_tower:
                self.move_disks()
            else:
                print(
                    "Sorry, can't move a disk to a position where it already "
                    "is!")
                text_turtle.goto(0, 300)
                text_turtle.pendown()
                text_turtle.write(
                    "Sorry, can't move a disk to a position where it already "
                    "is!",
                    align="center", font=("Arial", 20))
                text_turtle.penup()

                time.sleep(3)
                text_turtle.clear()
                self.cleanup()

    def move_disks(self):
        global text_turtle
        global moves_made
        moving_disk_turtle = self.origin_tower.pole_content[-1].disk_turtle
        moving_disk = self.origin_tower.pole_content[-1]

        # if the destination pole is not empty, assign variables
        # Variables needed for next if statement
        # crashes without if statement
        if (self.destination_tower.pole_content):
            width1 = self.origin_tower.pole_content[-1].width
            width2 = self.destination_tower.pole_content[-1].width

        # if the destination is empty, or if the lowest disk in the destination
        # has a bigger width than the disk you want to move to that place
        if (not self.destination_tower.pole_content) or (width1 < width2):
            print("in move_disks")
            self.origin_tower.pole_content.pop()
            self.destination_tower.pole_content.append(moving_disk)
            x_pos = self.destination_tower.x_pos
            position_in_tower = self.destination_tower.pole_content.index(
                moving_disk)
            y_pos = -90 + (20 * position_in_tower)
            moving_disk_turtle.goto(x_pos, y_pos)
            moves_made += 1
        else:
            print("Sorry, the disk on the destination pole is smaller")
            text_turtle.goto(0, 300)
            text_turtle.pendown()
            text_turtle.write(
                "Sorry, the disk on the destination pole is smaller.",
                align="center", font=("Arial", 20))
            text_turtle.penup()

            time.sleep(3)
            text_turtle.clear()

        self.wincondition_check()

    def cleanup(self):
        self.origin_tower = False
        self.destination_tower = False
        self.button_pressed = False
        print("cleanup done")

    def wincondition_check(self):
        global start_time
        # checkt of winconditie is bereikt
        # if the pole that has the tower is not the starter tower (avoid cheat)
        # and if the pole that has the tower is the same as the list with
        # disks (so if the pole has all disks, in order)
        if ((self.destination_tower != pole_list[0]) and (
                self.destination_tower.pole_content == disk_list)):
            # events that trigger after the user
            main_window.bye()
            root = tkinter.Tk()
            end_window = GameEndWindow(root, moves_made, start_time)
            root.mainloop()

        else:
            # events that trigger when the user hasnt won yet
            print("haven't won yet")
        self.cleanup()


class MoveButton:

    def __init__(self):
        self.width = 100
        self.length = 50
        self.x_pos = 0
        self.y_pos = 0
        self.referencing_pole = 0

    def draw_self(self, inst_turtle):
        inst_turtle.penup()
        inst_turtle.fillcolor("green")
        inst_turtle.goto(self.x_pos, self.y_pos)
        inst_turtle.pendown()
        inst_turtle.shape("square")
        inst_turtle.shapesize(2, 8)


class PlayingFieldPole:

    def __init__(self):
        self.length = 140 + (amount_of_disks * 20)
        # Default width is 20
        self.pole_content = []
        # Absolute coordinates in Screen
        self.x_pos = 0
        self.y_pos = 0

    def draw_self(self, inst_turtle):
        inst_turtle.penup()
        inst_turtle.fillcolor("black")
        inst_turtle.goto(self.x_pos, self.y_pos)
        inst_turtle.pendown()
        inst_turtle.shape("square")
        inst_turtle.shapesize(10, 1)


class TowerDisk:

    def __init__(self):
        # Calculated in create_disks
        self.width = 0
        # Default height is 20
        self.x_pos = 0
        self.y_pos = 0
        self.disk_turtle = None

    def draw_self(self, inst_turtle, i):
        inst_turtle.penup()
        inst_turtle.fillcolor(255 - (i * 30), 255 // (i + 1 * 20),
                              0 + (i * 30))
        inst_turtle.goto(self.x_pos, self.y_pos)
        inst_turtle.pendown()
        inst_turtle.shape("square")
        inst_turtle.shapesize(1, 7 - (0.5 * i))


def create_poles():
    for i in range(3):
        # Creates the poles in memory
        pole_list.append(PlayingFieldPole())
        pole_list[i].x_pos = -300 + (300 * i)
        pole_list[i].y_pos = 0

        # Turtle
        pole_turtle_list.append(turtle.Turtle(visible=True))
        pole_turtle_list[i].speed("fastest")
        pole_list[i].draw_self(pole_turtle_list[i])


def create_disks():
    for i in range(amount_of_disks):
        # Creates disks in memory
        disk_list.append(TowerDisk())
        disk_list[i].width = amount_of_disks - (1 * i)
        disk_list[i].x_pos = -300
        # 20 = height
        disk_list[i].y_pos = -90 + (20 * i)

        # turtle
        disk_turtle_list.append(turtle.Turtle(visible=True))
        disk_turtle_list[i].speed("fastest")
        disk_list[i].draw_self(disk_turtle_list[i], i)

        # UML: makes disk aware of turtle
        disk_list[i].disk_turtle = disk_turtle_list[i]

        disk_turtle_list[i].penup()
    pole_list[0].pole_content = list(disk_list)


def create_buttons():
    for i in range(3):
        # Creates the buttons in memory
        move_button_list.append(MoveButton())
        move_button_list[i].x_pos = -300 + (300 * i)
        move_button_list[i].y_pos = -200
        move_button_list[i].referencing_pole = pole_list[i]

        # Create turtle for each instance
        move_button_turtle_list.append(turtle.Turtle(visible=True))
        move_button_turtle_list[i].speed("fastest")
        move_button_list[i].draw_self(move_button_turtle_list[i])


def check_button_clicked():
    # instead of x going from -600 to 600, from 0 to 1200
    # -50 so it takes into account button offset from edge of screen
    move_button_turtle_list[0].onclick(DiskMoveHelper.button_zero)
    move_button_turtle_list[1].onclick(DiskMoveHelper.button_one)
    move_button_turtle_list[2].onclick(DiskMoveHelper.button_two)


def main():
    global start_time
    start_time = time.time()
    create_poles()
    create_disks()
    # draw_disks()
    create_buttons()
    print(pole_list[0].pole_content)
    print(disk_turtle_list)
    check_button_clicked()
    # This makes sure the program doesn't quit on its own
    turtle.mainloop()


while True:
    # Pop-up window for level selection
    root = tkinter.Tk()
    start_window = GameStartWindow(root)
    root.mainloop()

    # Deceleration of global variables
    moves_made = 0

    pole_list = []
    pole_turtle_list = []

    # Biggest to smallest
    disk_list = []
    disk_turtle_list = []

    move_button_list = []
    move_button_turtle_list = []

    amount_of_disks = int(start_window.chosen_level)

    main_window = turtle.Screen()
    main_window.setup(1200, 700, None, None)
    main_window.title("Towers of Hanoi")
    main_window.colormode(255)
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    turtle.speed('fastest')
    DiskMoveHelper = DiskMoveHelper()
    main()
