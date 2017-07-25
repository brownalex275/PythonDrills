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
        c.execute('INSERT INTO times(datestamp) VALUES(datetime(CURRENT_TIMESTAMP,"localtime"));')
        c.execute('SELECT datestamp FROM times WHERE ROWID = (SELECT MAX(ROWID) FROM times);')
        start = c.fetchone()
        conn.commit()
    conn.close()
    self.entry_last.config(state='!disabled')
    self.entry_last.insert(0, start[0])
    self.entry_last.config(state='disabled')
    self.entry_status.config(state='!disabled')
    self.entry_status.insert(0, 'Press start')
    self.entry_status.config(state='disabled')

def last_24(self,src,destin):
    conn = sqlite3.connect('lastrun.db')
    with conn:
        c = conn.cursor()
        c.execute('INSERT INTO times(datestamp) VALUES(datetime(CURRENT_TIMESTAMP,"localtime"));') #insert the current local time the program was ran into the table
        conn.commit()
        c.execute('SELECT datestamp FROM times WHERE ROWID = (SELECT MAX(ROWID) - 1 FROM times);') #select the last time the user saw that the program was run
        now = c.fetchone()
        c.execute('SELECT COUNT(*) FROM times ') #select how many times the program was ran
        count = c.fetchone()
    conn.close()
    prevRun = dt.datetime.strptime(now[0],'%Y-%m-%d %H:%M:%S') #retrieve last time the program was run from the table and convert it into python datetime data type
    dest = destin #where the copied files will go
    source = src
    if count[0] == 2: #if the program was ran for the first time do the following
        for root, dirs, files in os.walk(source):  # grab the file locations
            for item in files:
                path = os.path.join(root, item)
                st = os.stat(path)
                mtime = dt.datetime.fromtimestamp(st.st_mtime)  # grab the modified times for each files
                if item.endswith(".txt"): #copy all .txt files to the folder because this is the first time the program was ran
                    print('%s modified %s' % (path, mtime))
                    shutil.copy(path, dest)  # copy files that were modified less than 24 hours ago
    else:
        for root, dirs, files in os.walk(source): #grab the file locations
            for item in files:
                path = os.path.join(root,item)
                st = os.stat(path)
                mtime = dt.datetime.fromtimestamp(st.st_mtime) #grab the modified times for each files
                if item.endswith(".txt") and mtime > prevRun: #if a file was modified after the last time the program ran it is copied into the folder
                    print('%s modified %s' % (path, mtime))
                    shutil.copy(path, dest)
    print('All modified files were copied successfully')
    self.entry_last.config(state='!disabled')
    self.entry_last.delete(0,END)
    self.entry_last.insert(0,now[0])
    self.entry_last.config(state='disabled')
    self.entry_status.config(state='!disabled')
    self.entry_status.delete(0, END)
    self.entry_status.insert(0, 'Files were successfully copied!')
    self.entry_status.config(state='disabled')




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