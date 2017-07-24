import shutil
import os

folder = '/Users/nygfan72/Desktop/Folder A/'
dest = '/Users/nygfan72/Desktop/Folder B'

files = os.path.dirname(folder)
folders = os.listdir(folder)
print(files)
for item in folders:
    print('file moved from ' + files+ '/' + str(item))
    source = files + '/' + str(item)
    shutil.move(source,dest)
