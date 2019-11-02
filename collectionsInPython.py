from array import array

names = ['Aishwarya', 'Alpa', 'Ashok', 'Bhaumeek']
print(names)
print(len(names))

names.insert(0, 'Someone')
print(names)

names.sort()
print(names)

females = names[0:2]
print(females)

grades = []
grades.append(99)
grades.append(98)
grades.append(97)

print(grades)
print(grades[1])

numbers = array('d')
numbers.append(99)
numbers.append(100)
numbers.append(98)

print(numbers)
print(numbers[1])

Aishwarya = {'first_name' : 'Aishwarya'}
Aishwarya['last_name'] = 'Solanki'
Dharmesh = {'first_name' : 'Dharmesh', 'last_name' : 'Gangani'}
print(Aishwarya)
print(Dharmesh)

Manager_employee = [Aishwarya, Dharmesh]
print(Manager_employee)
