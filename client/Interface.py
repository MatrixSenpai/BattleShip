from tkinter import *


class Window(Frame):

    master: Tk

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.__init_window()

    def __init_window(self):
        self.master.title("Battleship")
        self.pack(fill=BOTH, expand=1)

        self.__init_menu()

    def __init_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        main = Menu(menu)
        main.add_command(label="New Game (Online)", command=self.master.connect())
        main.add_command(label="New Game vs Computer (Offline)")
        main.add_command(label="Load Game vs Computer (Offline)")

        save = Menu(menu)
        save.add_command(label="Save Current Game")

        menu.add_cascade(label="Game", menu=main)
        menu.add_cascade(label="Save", menu=save)


class App(Tk):

    window: Window

    def __init__(self):
        Tk.__init__(self)

        self.__setup_size()

        self.window = Window(master=self)

    def __setup_size(self):
        height = 800
        width = 1000

        position_x = int(self.winfo_screenwidth()/2 - height/2)
        position_y = int(self.winfo_screenheight()/2 - width/2)

        self.geometry("%dx%d-%d+%d" % (width, height, position_x, position_y))
        self.resizable(0, 0)

    def connect(self):
        print("Connecting")


if __name__ == "__main__":
    g = App()
    g.mainloop()
