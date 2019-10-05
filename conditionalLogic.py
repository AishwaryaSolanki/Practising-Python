country = input('Enter your country name: ')

if country.lower() == 'india':
    print('Oh, look an Indian!!')
elif country.lower() == 'canada':
    print('Oh, look a Canadian!!')
else:
    print('The world is our family!!')

price = input('How much did you pay for your last meal: ')
price = float(price)

if price >= 100:
    tax = 5
else:
    tax = 0
print('Tax is ' + str(tax) + '%')

if country.lower() == 'india':
    state = input('Enter your state: ')
    if state.lower() == 'gujarat':
        print('Hello, kem chho?')
    elif state.lower() == 'maharashtra':
        print('Hello, kasa kaai?')
    else:
        print('Hello, How are you?')
elif country.lower() == 'germany':
    print('Hallo, Wei gehts?')
else:
    print('Hello, how are you?')

number = input('Which is your favourite number: ')

if int(number) in (5, 7, 255):
    print('Ah, good choice')
elif 8 <= int(number) <= 11:
    print('Amazing choice!')
else:
    print('That is my favourite number as well!')
