from tkinter import *
from tkinter import ttk
import filedb_func
import sqlite3
import datetime as dt


def load_gui(self):
    self.style = ttk.Style() #style widgets
    self.style.configure('TFrame', background='#355C7D')
    self.style.configure('TButton', background='#F8B195', font=("Helvetica", 10, "bold"))
    self.style.configure('TLabel', background='#355C7D', foreground='#F8B195', font=("Helvetica", 10, "bold"))

    self.frame_main = ttk.Frame(self.master) #create frame to hold widgets
    self.frame_main.pack(fill=BOTH)

    ttk.Label(self.frame_main, text="Which folder contains the modified files?").grid(row=0, column=0, sticky = 's', pady= 10) #create label and entry for folder to watch
    self.entry_modified = ttk.Entry(self.frame_main, width=20)
    self.entry_modified.grid(row=1, column=0, sticky='n',padx=20)



    ttk.Label(self.frame_main, text="Where should the files be copied?").grid(row=3, column=0,sticky= 's', pady=10) #create label and entry for folder to copy to
    self.entry_copied = ttk.Entry(self.frame_main, width=20,)
    self.entry_copied.config(state='!disabled')
    self.entry_copied.grid(row=4, column=0,padx=20, sticky ='n')



    self.btn_chooseMod = ttk.Button(self.frame_main, text='Choose File', command=lambda: filedb_func.choose_mod(self)) #create buttons for choosing watch and copy folders
    self.btn_chooseMod.grid(row=2, column=0, pady=10)
    self.btn_chooseCopy = ttk.Button(self.frame_main, text='Choose File', command=lambda: filedb_func.choose_copy(self))
    self.btn_chooseCopy.grid(row=5, column=0,pady=10)
    self.btn_start = ttk.Button(self.frame_main, text='Start', command=lambda: filedb_func.last_24(self,src=self.entry_modified.get(),destin = self.entry_copied.get()))
    self.btn_start.grid(row=2, column=1, padx=20)
    filedb_func.create_db(self)












