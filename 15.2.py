# Toan tu hash object va unhash object:
# Su khac nhau giua s = s + i, s += i;
'''
s1 = 'how'
s2 = 'free'
print(id(s1))
print(id(s2))
s1 = s1 + 'python'
s2 += 'python'
print(id(s1))
print(id(s2))
'''
##############
'''
s1 = [1,2]
s2 = [3,4]
print(id(s1))
print(id(s2))
s1 = s1 + [0]
s2 += [0]
print(id(s1))
print(id(s2))
'''
################
s1 = [1,2]
s2 = [3,4]
s3 = [5,6]
print(s1,s2,s3)
print(id(s1))
print(id(s2))
s1 = s1 + s3
s2 += s3 # <=> s2.__add__(s3)
print(id(s1))
print(id(s2))

# Su khac biet giua toan tu hash object va unhash object:
print('----------s=s+i * s+=i----------')
s = [1,2]
print(id(s))
s = s + [3]
print(id(s))

t = [1,2]
print(id(t))
t += [3]
print(id(t))
t.__add__([4])
print(id(t))

