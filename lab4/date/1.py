import datetime

x = datetime.datetime.now()

five_days = x - datetime.timedelta(days=5)

print(five_days)