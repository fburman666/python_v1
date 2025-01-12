import datetime
from datetime import date
print("Dagens datum är " + str(date.today()))
nextweek = date.today() + datetime.timedelta(days=7)
print("Datum om 7 dagar är " + str(nextweek))