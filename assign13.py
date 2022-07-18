#Find yesterday’s, today’s and tomorrow’s date

import datetime

presentdate=datetime.date.today()
yesterday=presentdate - datetime.timedelta(1)
tomorrow=presentdate + datetime.timedelta(1)

print(yesterday)
print(presentdate)
print(tomorrow)