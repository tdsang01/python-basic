# Chu y MODE khi open file
# Cau lenh with

# open() # mode
file_object = open('test.txt', mode='r')
print('---open()---')
print(file_object)
print(type(file_object))

# read()
print('---read()---')
#data = file_object.read() # read() # param: size: 1,2,... -1 
# khi doc file xong, con tro se nhay den vi tri size.
#print(data)

# readline() # doc tung dong
# readlines() 

# list, tuple # dua con tro ve cuoi file
print('---list, tuple,...')
#data = list(file_object) # ['Hello\n', 'How are you?\n', 'Bye bye']
#print(data)
#data = tuple(file_object) # ('Hello\n', 'How are you?\n', 'Bye bye')
#print(data)

# write() # CHU Y CHU Y:  mode
print('---write()---')
#data = file_object.write('\nWrite new line')
#print(data)

# seek() # dich chuyen con tro
data1 = file_object.read()
print('data1: ', data1)
data2 = file_object.read()
print('data2: ',data2)
file_object.seek(10)
data2 = file_object.read()
print('data2: ',data2)
''' 
data1:  Hello
How are you?
Bye bye
Write new line
data2:
data2:  are you?
Bye bye
Write new line
'''

# cau lenh with


# close()
file_object.close()


















