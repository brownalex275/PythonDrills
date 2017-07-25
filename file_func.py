import shutil
import os
import datetime as dt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import file_gui
import file_main
import io



def last_24(self,stop,src,destin):
    buffer = io.StringIO() #saves shell output as a file
    if stop:
        now = dt.datetime.now() #get current time
        limit = dt.timedelta(hours = 24) #set 24 hour limit for files to be modified in for copying
        dest = destin #where the copied files will go
        source = src
        for root, dirs, files in os.walk(source): #grab the file locations
            for item in files:
                path = os.path.join(root,item)
                st = os.stat(path)
                mtime = dt.datetime.fromtimestamp(st.st_mtime) #grab the modified times for each files
                if now - mtime < limit:
                    print('%s modified %s' % (path, mtime),file=buffer) #sends output to a file
                    shutil.copy(path, dest) #copy files that were modified less than 24 hours ago
        print('All modified files were successfully copied.',file=buffer)
        output = buffer.getvalue()
        self.text_results.delete('1.0',END)
        self.text_results.insert(END,output)
        self.after(300000,lambda: last_24(self,stop=True,src=source,destin =dest)) #waits 5 minutes before checking again
    else: print('Program stopped.',file=buffer)
    output = buffer.getvalue() #saves file contents to a variable
    self.text_results.delete('1.0', END)
    self.text_results.insert(END, output) #output file contents to the text widget

def ask_quit(self): #asks user if they want to exit if red x is clicked on mac
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #This closes app
        self.master.destroy()
        os._exit(0)

def choose_mod(self): #lets user choose which file to watch for modified files
    filename = filedialog.askdirectory()
    self.entry_modified.delete(0,END)
    self.entry_modified.insert(0,filename)

def choose_copy(self): #lets user choose which file to move modified files to
    filename = filedialog.askdirectory()
    self.entry_copied.delete(0,END)
    self.entry_copied.insert(0,filename)