#Program written in Python 2.7 with the purpose of determining if a building in London and NY is open based on the time in Portland
from datetime import datetime #import required modules to get current time
from pytz import timezone
pdt = timezone('US/Pacific')
portland = datetime.now(pdt)
hour_port = portland.hour
london = int(hour_port) + 8 #convert the current hour in portland to london and new york time
ny = int(hour_port) + 3

if london < 9 or london > 21: #decide if the buildings are open or closed based on the converted times
    print('The London branch is closed.')
else:
    print('The London branch is open.')


if ny < 9 or ny > 21:
    print('The New York branch is closed.')
else:
    print('The New York branch is open.')




