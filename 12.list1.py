a = [1,2, '3', 'four', ['5', 6]]
print(a)

b = [i for i in range(10)]
print(b)

c = [i * 2 for i in range(1,4)]
print(c)

d = [[i, i * 2, i * 3] for i in range(2,5)]
print(d)

# list(interable)
e = list('hello')
print(e)

# +
f = [1,2]
f += ['one']
print(f)

g = list('hello')
g += ['how are you']
print(g)
 
h = [1,2, ['1']]
h *= 3
print(h)

print('1' in h)

i = [1,2,'3', 'c', 'd', [5, 'g']]
j = i[1: 3]
k = i[: 9]
print(j) # [2, '3']
print(k) # [1, 2, '3', 'c', 'd', [5, 'g']]
print(i[:3]) # [1, 2, '3']
print(i[4:]) # ['d', [5, 'g']]
print(i[::-1]) #[[5, 'g'], 'd', 'c', '3', 2, 1] # -1: buoc nhay
print(i[::-2]) # [[5, 'g'], 'c', 2] # -2: buoc nhay
print(i[::-3]) # [[5, 'g'], '3']

# matrix
matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix1)
matrix2 = matrix1
print(matrix1)
print(matrix2)
matrix2[0] = 'Hello'
print(matrix1)
print(matrix2)
matrix3 = list(matrix1)
matrix3[0] = 'Ok'
print(matrix1)
print(matrix2)
print(matrix3)

print('---------------------')
ma1 = [[1,2,3],[4,5,6]]
ma2 = list(ma1)
print(ma1)
print(ma2)
ma2[0][1] = 'Hele'
print(ma1)
print(ma2)

















