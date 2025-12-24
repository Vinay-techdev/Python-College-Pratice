from datetime import datetime, timedelta

# class
dateTime = datetime.now()
print("Current Date and time ", dateTime)

date = datetime(2025, 2, 11, 15, 30, 45)
print("Format(yy/mm/dd) date :", date)

from datetime import time
t = time(10, 15, 30)
print(t)

curr = datetime.now()
futur_date = curr + timedelta(days=7)
print(futur_date)

futur_time = curr + timedelta(hours=2, minutes=20)
print(futur_time)

# formating date and time
strDateTime = curr.strftime('%y-%m-%d-%S-%M-%H')
print(strDateTime)

dt = date.strftime("%I:%M:%p")
print(dt)