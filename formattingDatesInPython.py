from datetime import datetime, timedelta

birthday = input('Enter your birthday in dd/mm/yyyy: ')
print('Your birthday is ' + str(birthday))

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Your birthday date is ' + str(birthday_date))

one_day = timedelta(days = 1)
birthday_eve = birthday_date - one_day
print('Birthday eve is ' + str(birthday_eve))
