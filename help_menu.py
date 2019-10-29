from tkinter import *
from tkinter.messagebox import *
import sys


class Help():
    def about(root):
        showinfo(title="About", message="ProOffice write is an open source text editor made with the tkinter GUI module pre-installed into python. Good news- you can edit and redistribute free of charge with the conditon that you keep the info included intact/unaltered")
		
def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
