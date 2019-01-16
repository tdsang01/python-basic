"""Duoc gioi han boi cap ngoac ()
 Chua duoc moi gia tri
 Toc do truy xuat nhanh hon list
 Chiem dung luong bo nho nho hon list
 Bao ve du lieu khong bi thay doi
 Co the dung lam key cua dictionary"""

 # Toan tu cua tuple giong voi toan tu cua chuoi
 # Toan

 # tuple
tup = (1,)
print(tup)
print(type(tup))

a = tuple((1,2,3))
print(a)

a = (i for i in range(10))
print(a) # <generator object <genexpr> at 0x7f06f77e59e8>
a = tuple(a)
print(a) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tuple(i for i in range(20) if i % 2 == 0))

# +
print('---Toan tu +---')
tup = (1,4,5)
tup += (3,6)
print(tup)

# *
print('---Toan tu *---')
tup *= 3
print(tup)

# in
print(1 in tup) # True

# indexing
print(tup[3]) # 3

# len()
print(len(tup))

# last element
print(tup[-1])

# reverse tuple
print(tup[::-1])

# tup[0] = 'One' => error

# tuple matrix, like list ((), (), ())

a = ([1,2,3]) # => list
print(a, type(a)) 

# count()

# index() 































