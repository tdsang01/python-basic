# while loop
print('---While loop---')
length = 3
iter_ = (x for x in range(length))
c = 0
while c < length:
    print(next(iter_))
    c += 1

# try-block
print('Try block')
while 1:
    try:
        print(next(iter_))
    except StopIteration:
        print('error')
        break
# For loop
# for variable_1, var_2, ..., var_n in sequence: # sequence: iterable object
    # for-block
print('For loop')
iter_ = (x for x in range(3))
for value in iter_:
    print('->', value)

# For loop with dictionary
print('---dictionary---')
dic = {'name': 'Td', 'age': 20, 'address': 'Dn'}
for item in dic:
    print('item: ', item)
for key, value in dic.items():
    print('Key: ', key, ' Value: ', value)
    if key == 'age':
        break

# For else # Hết vòng lặp thì chạy else.
print('---for else---')
for k in (1, 2, 3):
    print(k)
else:
    print('Done')

