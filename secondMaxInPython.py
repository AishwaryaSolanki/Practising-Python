n = 5
arr = [2, 3, 6, 6, 5]

maximum = arr[0]
second_max = arr[0]

for i in range( 0, len(arr)):
    if arr[i] >= maximum:
        maximum = arr[i]

for i in range(0, len(arr)):
    if arr[i] >= second_max and second_max < maximum:
        second_max = arr[i]
        print(second_max)

print(second_max)
