# Function

print('# basic function')


def first_function():
    print('Hello')


print(first_function(), type(first_function()))
# Hello
# Hello
# None <class 'NoneType'>
print(first_function, type(first_function))  # <function first_function at 0x7f8d0543be18> <class 'function'>

print('# parameter function')


def func_parameter(name, age):
    print('My name is', name)
    print('I\'m :', age)


func_parameter('Sang', 25)

