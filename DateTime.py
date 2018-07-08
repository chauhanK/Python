import datetime

#Date
d =datetime.date(2018,7,7)
print(d)

tday =datetime.date.today()

print(tday.year)
tday.weekday()

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

#Time
t=datetime.time(9,30,45)
print(t.hour)

#DateTime
dt = datetime.datetime(2018,7,7,6,55,45,10000)
print(dt)

dt_today = datetime.datetime.today() # can not pass timezone
dt_now = datetime.datetime.now() # can pass timezone here
dt_utcnow=datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)