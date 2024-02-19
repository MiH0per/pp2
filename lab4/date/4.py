import datetime

x=datetime.datetime(2024, 1, 1, 12, 0, 0)
y = datetime.datetime(2024, 1, 2, 12, 0, 0)

dif = (y - x).total_seconds()
print(dif)
