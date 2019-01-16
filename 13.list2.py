a = [1,2,3,4,5,4]
print(a)
c = a.count(4) # Dem so lan xuat hien cua phan tu 4
print(c)

print(a.index(4)) # Vi tri xuat hien dau tien cua phan tu 4 o trong list.
                  # Neu ko co thi throw error

# copy() # tao ra 1 ban sao.

# clear() 
d = a
d.clear()
print(a) # []
print(d) # []
d = a.clear()
print('---clear()---')
print(a) # []
print(d) # None

# append()
a = [1,2,3]
print(a)
a.append(4)
print(a)

# extend()
a.extend([4,5,[6,7]])
print(a)

# insert(index, value) Insert phan tu value vao vi tri index
a.insert(10, 'Ahihi') # Neu index > len(a) => insert vao cuoi cung
print(a)

# pop()
a = [1,2,3]
c = a.pop(1)
print(a)
print(c)

# remove()
print('---remove()---')
a = [1,2,1,3]
c = a.remove(2) # throw error if 2 not in list
print(a)
print(c)

# reverse() # Dao nguoc list

# sort(key=None, reverse=False) # sap xep
print('---sort()---')
a = [1,5,0,3,6,2,6,22,0] # De sap xep duoc thi tat ca cac phan tu phai cung keiu du lieu
print(a)
a.sort(reverse=True) # Giam gian
print(a)















