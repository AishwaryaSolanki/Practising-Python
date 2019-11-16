def logger(func):
    def wrapper_func():
        print('Logging the function:')
        func()
        print('Done execution')
    return wrapper_func


@logger 
def sampleFunc():
    print('Inside Sample Function')

sampleFunc()
