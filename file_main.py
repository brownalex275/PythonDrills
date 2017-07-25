from tkinter import *
from tkinter import ttk
import file_func
import file_gui

class FTransfer(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master = master
        self.master.title("Copy Modified Files")
        self.master.resizable(False, False) #prevents screen from being resized
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_func.ask_quit(self)) #goes to askquit function
        file_gui.load_gui(self)


def main():
    root = Tk()
    style = ttk.Style()
    style.theme_use('clam')
    fTransfer = FTransfer(root)
    root.mainloop()


if __name__ == "__main__": main()
