print(r'Haizzz, \neu mot ngay nao do')

strA = 'Hello, how are you?'
strB = 'You'
strC = strA + strB
print(strC)
strD = strA * 2
print(strD) # Hello, how are you?Hello, how are you?

check = strB in strA
print(check) # false

print(strA[1]) # e
print(strA[3]) # l
print(strA[-2])# u

print(strA[len(strA)-1]) # ?

# cut string
str1 = strA[1:2]
print(str1) # e
print(strA[1:len(strA)]) # ello, how are you?
print(strA[1:None]) # ello, how are you?
print(strA[None:2]) # He
print(strA[None:None]) # Hello, how are you?
print(strA[:]) # Hello, how are you?

print(strA[None:None:2]) # Hlo o r o?
print(strA[None:None:-2]) # ?o r o olH

# Ep kieu
str3 = int('6') + 5
print(str3) # 11
print(int(6.9)) # 6
s4 = str(69) + '5' 
print(s4) # 695

s5 = 'HowKteam.com'
print(hash(s5)) # 2928394470554318598 # -8693619812024552415 # change after run again
''' 
=> Note: Khi chay 1 chuong trinh python thi gia tri cua ham hash() len
mot gia tri nhat dinh khong thay doi. Nhung gia tri do se thay doi 
neu nhu co lan chay tiep theo.
'''





















