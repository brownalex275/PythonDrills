import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import filedb_gui
import filedb_main
import sqlite3
import datetime as dt

def create_db(self):
    conn = sqlite3.connect('lastrun.db') #create new database named lastrun
    with conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS times(datestamp TEXT);') #create new table that will hold times in lastrun.db
        conn.commit()
    conn.close()
    insert(self)

def insert(self):
    conn = sqlite3.connect('lastrun.db')
    with conn:
        c = conn.cursor()
        current = dt.datetime.now()
        c.execute('INSERT INTO times(datestamp) VALUES(?)', (
        current.strftime('%Y-%m-%d %H:%M:%S'),))  # insert the current time files were copied
        conn.commit()
        c = conn.cursor()
        c.execute('SELECT datestamp FROM times ORDER BY datestamp DESC')
        newTime = c.fetchone()[0]
    c.close()
    self.label = ttk.Label(self.frame_main, text="Last time files were copied: " + str(newTime))
    self.label.grid(row=1, column=1, sticky='s')


def last_24(self,src,destin):
    dest = destin  # where the copied files will go
    source = src
    current = dt.datetime.now()
    prevRun = current - dt.timedelta(hours=24)
    for root, dirs, files in os.walk(source): #grab the file locations
        for item in files:
            path = os.path.join(root,item)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime) #grab the modified times for each files
            if item.endswith(".txt") and mtime > prevRun: #if a file was modified after the last time the program ran it is copied into the folder
                print('%s modified %s' % (path, mtime))
                shutil.copy(path, dest)
    insert(self)





def ask_quit(self): #asks user if they want to exit if red x is clicked on mac
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #This closes app
        self.master.destroy()
        os._exit(0)


def choose_mod(self): #lets user choose which folder to watch for modified files in
    filename = filedialog.askdirectory()
    self.entry_modified.delete(0,END)
    self.entry_modified.insert(0,filename)

def choose_copy(self): #lets user choose which folder to move modified files to
    filename = filedialog.askdirectory()
    self.entry_copied.delete(0,END)
    self.entry_copied.insert(0,filename)

