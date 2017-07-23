from datetime import datetime
from pytz import timezone
pdt = timezone('US/Pacific')
portland = datetime.now(pdt)
hour_port = portland.hour
london = int(hour_port) + 8
ny = int(hour_port) + 3

if london < 9 or london > 21:
    print('The London branch is closed.')
else:
    print('The London branch is open.')


if ny < 9 or ny > 21:
    print('The New York branch is closed.')
else:
    print('The New York branch is open.')




