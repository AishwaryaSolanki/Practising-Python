x = 0
y = 240

try: z = y / x
except ZeroDivisionError as e:
    print('Error caught: ZeroDivisionError')
except:
    print('Something went wrong')
finally:
    print('This runs on Success or Failure')
