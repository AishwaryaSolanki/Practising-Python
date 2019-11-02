from datetime import datetime

def print_date():
    print('Current date and time are: ')
    print(datetime.now())
    print()

def print_initials(name, upper_case_flag = True):
    if upper_case_flag:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

print_date()

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('Your initials are ' + print_initials(first_name, False) + '.' + print_initials(last_name))

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

year = int(input('Enter a year to check if its a leap year: '))
print(is_leap(year))
