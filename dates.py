from datetime import datetime, timedelta

current_date = datetime.now()
print('Current date is ' + str(current_date))

one_day =  timedelta(days = 1)
yesterday = current_date - one_day
print('Yesterday was ' + str(yesterday))

one_day =  timedelta(weeks = 1)
last_week = current_date - one_day
print('Last week was ' + str(last_week))

print('Today is ' + str(current_date.day) + '/' + str(current_date.month) + '/' + str(current_date.year))
