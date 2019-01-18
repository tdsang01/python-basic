'''
Duoc gioi han boi cap ngoac {}
Set khong chua phan tu trung lap
Set chi co the chua cac hasable object,
nhung chinh no khong phai la hashable object
=> Do do, khong the chua mot set trong mot set
Khong the tao empty set neu ko dung constructor

Set khong quan tam den vi tri cua phan tu nam trong set.
Nen viec indexing va cat set trong python khong duoc ho tro.
'''
s1 = {6,9}
print(s1)
print(type(s1))

s2 = {1, 2, 'Fee', (3, (4,3))}
print(s2)

# constructor set
print('---constructor---')
s3 = set([1,2,3]) # string, tuple, list
print(s3)
print(type(s3))

S = set()
print(S, type(S))


s4 = {'hello'}
print(s4, type(s4)) # {'hello'} <class 'set'>
s5 = set('hello world')
print(s5, type(s5)) # {' ', 'w', 'l', 'r', 'd', 'e', 'h', 'o'} <class 'set'>

print('---------------Toan tu----------------')

# Toan tu in
print({ i for i in range(3)})
print({1,2,3,4} in {1,2,3,4})

# Toan tu - # chi tra ve nhung phan tu ton tai trong set1 ma khong ton tai trong set2
set1 = {1,2,3,4}
set2 = {2,4}
print(set1 - set2) # {1, 3}

# Toan tu & # Vua ton tai trong ca 2 set
print({1,2,3} & {3,4,5}) # {3} (1)

# Toan tu | # Tong 2 set
print({1,2,3} | {3,4,5}) # {1, 2, 3, 4, 5} (2)

# Toan tu xor (^)
print({1,2,3} ^ {3,4,5}) # (2) - (1)

# Cac phuong thuc trong set: 
# clear() -> empty set()

# pop() Pop phan tu dau tien
s1 = {1,2,3,4}
s2 = s1.pop()
print(s1, s2) # {2, 3, 4} 1
print(1,2 in {2,3,4})

# remove() 
print('---remove()---')
set1 = {1,3,4,6,7}
print(set1)
# set1.remove(2) # Error
print(set1.remove(4))
print(set1)

# discard() # Neu ko co thi ko bi loi
print('---remove()---')
set1 = {1,3,4,6,7}
print(set1)
# set1.remove(2) # Error
print(set1.remove(4))
print(set1)

# discard() # Giong voi remove() nhung ko throw error.
print(set1.discard(6), set1)

# copy()

# add()


