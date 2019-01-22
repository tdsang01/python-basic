print('hello', 'world')

#  Parameter
#  sep (chia ra, phân ra)
print('--- parameter sep ---')
print('Hello', 'Python', 'Course', sep='---')  # Hello---Python---Course

# end
print('--- parameter end ---')
print('line 1', end='|')
print('line 2')
print('line 3')

#  sleep()
from time import sleep
print('start...')
sleep(1)
print('end...')

print('start...', end='')
sleep(1)
print('end...')

#  file
print('---print file by open file---')
with open('test1.txt', 'w') as f:
    print('Printed by print function', file=f)


#  flush # default False # liên quan trực tiếp đến parameter end
#  flush=True => Yêu cầu bộ đệm xuất những gì có trong bộ đệm ra.
print('---parameter flush ---')
print('start...xxx...', end='', flush=True)
sleep(1)
print('end...')

#  So sánh print trong Python 3x và 2x
#  3x: Hàm, 2x: Câu lệnh.
print('---Print funny---')
name = 'Panda.'
great = 'Hello! My name is '
for char in great + name:
    print(char, end='', flush=True)
    sleep(0.2)
