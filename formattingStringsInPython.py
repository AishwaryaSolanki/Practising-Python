first_name = input('Enter first name: ')
last_name = input('Enter last name: ')

output = 'Hello, ' + first_name + ' ' + last_name
print(output)

output = 'Hello, {} {}'.format(first_name, last_name)
print(output)

output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)

output = f'Hello, {first_name} {last_name}'
print(output)
