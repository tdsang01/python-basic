a = id(5)
print(a, type(a))

a = 'Hello'
b = id(a)
print('b: ',b)
print('id(a):', id(a))
print(b == id(a)) # b luon luon bang id(a)

'''
Ham id() trong python tra ve gia tri la 1 so nguyen. 
Gia tri nay la duy nhat, va la hang so khong thay doi
trong suot chuong trinh (Co the noi id() tra ve dia chi 
cua gia tri doi tuong trong bo nho)
print(id(5)) # KHONG THAY DOI khi CHAY LAI CHUONG TRINH. (so nguyen la khong thay doi)
print(id('string')) # thay doi. string, list, tuple,...
'''
# Toan tu
# => Moi toan tu cua moi doi tuong se co phuong thuc di kem.
n = 69
print(n)
print(n+1)
print(n.__add__(1))
print(n)
