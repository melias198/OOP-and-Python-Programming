#Return function from the function which is called inner function
def timer():
    def inner():
        print('This is Start')
        print('This is End')
        return 'Returinig from inside function'
    return inner

print(timer()())


# Function as a perameter which is called wrapper function
def func(work):
    print('Work Starting')
    work()
    print('Work Ended')


def do():
    print('Working With Python As A Djago Developer')


func(do)