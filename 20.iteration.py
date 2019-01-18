itera = [x for x in range(3)]
print(itera)
print(type(itera))
iterator = itera.__iter__()
print('aaaaaaaa: ', iterator)
print('bbbbbbbb: ', type(iterator))

itera = (x for x in range(3)) # generator object. Ko the truy xuat truc tiep bang index, chi co the truy xuat bang ham next()
print(itera)
print(type(itera))
print(next(itera)) # 0
print(next(itera)) # 1
print(next(itera)) # 2
#print(next(itera)) # error StopIteration

# tup = tuple(itera)
# print('tup: ', tup)
# print('tup[0]: ',tup[0])

# Mot so ham ho tro cho iterable object
# note: Cac ham nay buoc phai lay cac gia tri cua iterable de xu ly
# Do do neu dua vao mot iterator, thi se khong su dung iterator do duoc nua.

print('---Mot so ham ho tro---')
print('---sum()---')
itera = (x for x in range(3))
print(itera, type(itera))

# sum() # chi dung trong iterator kieu nguyen
print('---sum()---')
print(sum(itera, 5)) # 3 # start=5 => 8
# sau khi sum thi ko the dung ham next()
#print(next(itera)) # StopIteration
print(itera, type(itera))

# max()
print('---max()---')
itera = [1,2,3]
print(max(itera)) # 3
print(max([], default='Default value')) # Default value
print(max(1,23,4,4)) # 23 # ham max() co the nhan 1 list argument

# min()
print('---min()---')

# sorted()
itera = [4,21,5,5,1]
print(sorted(itera)) # [1, 4, 5, 5, 21]
print(sorted(itera, reverse=True)) # [21, 5, 5, 4, 1]


























