#Program written in Python 2.7 with the purpose of moving files from a desktop folder A to a desktop folder B
import shutil
import os

folder = '/Users/nygfan72/Desktop/Folder A/'
dest = '/Users/nygfan72/Desktop/Folder B'

files = os.path.dirname(folder) #get directory name of files in folder A
folders = os.listdir(folder) #get list of items in folder A
print(files)
for item in folders: #move files from folder A to folder B and print the locations of the moved files
    print('file moved from ' + files+ '/' + str(item))
    source = files + '/' + str(item)
    shutil.move(source,dest)
