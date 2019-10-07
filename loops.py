
print('Counting from 1 to 10 like...')

for i in range(1, 5):
    print(i)

i += 1

while i < 11:
    print(i)
    i += 1

people = ['Aishwarya', 'Dharmesh']
for name in people:
    print(name)

index = 0
while index < len(people):
    print(str(index) + ' -> ' + people[index])
    index+=1
