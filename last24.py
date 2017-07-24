import shutil
import os
import datetime as dt
now = dt.datetime.now()
last = now - dt.timedelta(hours = 24)
dest = '/Users/nygfan72/Documents/Python Course/Copied Files'

for root, dirs, files in os.walk('/Users/nygfan72/Documents/Python Course/Modified Files'):
    for item in files:
        path = os.path.join(root,item)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > last:
            print('%s modified %s' % (path, mtime))
            shutil.copy(path, dest)
print 'All files were successfully copied.'