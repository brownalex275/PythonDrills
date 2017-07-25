#Program written in Python 2.7 with the purpose of copying files that had been modified in the past 24 hours
#to a new folder, where they will be scheduled to be sent somewhere else for storage
import shutil
import os
import datetime as dt
import time
stop = True
while stop:
    now = dt.datetime.now() #get current time
    limit = dt.timedelta(hours = 24) #set 24 hour limit for files to be modified in for copying
    dest = '/Users/nygfan72/Documents/Python Course/Copied Files' #where the copied files will go

    for root, dirs, files in os.walk('/Users/nygfan72/Documents/Python Course/Modified Files'): #grab the file locations
        for item in files:
            path = os.path.join(root,item)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime) #grab the modified times for each files
            if item.endswith(".txt") and now - mtime < limit:
                print('%s modified %s' % (path, mtime))
                shutil.copy(path, dest) #copy files that were modified less than 24 hours ago
    print 'All modified files were successfully copied.'
    time.sleep(300) #waits 5 min before checking again