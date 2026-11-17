import time
import datetime
now = datetime.datetime.now()
print("Current Date and Time :",now)
print("Current year :",now.year)
print("Month of the year :",now.month)
print("Week number of the year :",now.isocalendar()[1])
print("Day of the year :",now.strftime("%A"))
print("Day of the year :",now.strftime("%j"))
print("Day of the month :",now.day)
print("Day of the week :",now.weekday())
