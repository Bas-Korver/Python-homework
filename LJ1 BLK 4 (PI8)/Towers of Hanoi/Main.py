import tkinter
import sys
import turtle


class UserInputWindow:
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

root = tkinter.Tk()
my_gui = UserInputWindow(root)
root.mainloop()
print(my_gui.a)

class Disc(turtle.RawTurtle):
    def __init__(self, cv):
        turtle.RawTurtle.__init__(self, cv, shape="square", visible=False)
        self.pu()
        self.goto(-140,200)

    def config(self, k, n):
        self.hideturtle()
        f = float(k+1)/n
        self.shapesize(0.5, 1.5+5*f)
        self.fillcolor(f, 0, 1-f)
        self.showturtle()