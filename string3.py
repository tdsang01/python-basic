# 
a = 'Hello %s %s' %('world', '2')
print(a)

b = '%s %s'
c = b %('one', 'two')
print(c) # one two
e = '%s %s'
f = e %('e','f')


class Something:
    def __repr__ (s):
        return '__REPR__'

    def __str__ (s):
        return '__STR__'    


st = Something()
print('%s %r' %(st, st)) # __STR__ __REPR__


fl = 3.45463456345
print('%.2f' %(fl))

# f-string
name = 'Jarvis'
age = '25'
print('My name is {name}, I\'m {age} old') # My name is {name}, I'm {age} old
print(f'My name is {name}, I\'m {age} old') # My name is Jarvis, I'm 25 old

# format string
z = 3
s1 = 'a: {}, b: {}, c: {}'.format('x','y',z)
print(s1) # a: x, b: y, c: 3
s2 = 'a: {2}, b: {0}, c: {1}'.format('x','y',z)
print(s2) # a: 3, b: x, c: y
s3 = '1: {one}, 2: {two}'.format(two='222', one=111)
print(s3) # 1: 111, 2: 222
s4 = '---{:*<10}---'.format('Jarvis')
print(s4) # ---Jarvis****---
s5 = '---{:*>10}---'.format('Jarvis')
print(s5) # ---****Jarvis---
s6 = '---{:*^10}---'.format('Jarvis')
print(s6) # ---**Jarvis**---

row1 = '+ {:-^11} + {:-^19} + {:-^15} +'.format('a','b','c')
print(row1)
row2 = '| {:^11} | {:^19} | {:^15} |'.format('ID','Name','Address')
print(row2)
row3 = '| {:^11} | {:^19} | {:^15} |'.format('01','Tony Stack','American')
print(row3)
row4 = '| {:^11} | {:^19} | {:^15} |'.format('02','Odin Thor','Asgard')
print(row4)
rowN = '+ {:-^11} + {:-^19} + {:-^15} +'.format('x','y','z')
print(rowN)
'''
+ -----a----- + ---------b--------- + -------c------- +
|     ID      |        Name         |     Address     |
|     01      |     Tony Stack      |    American     |
|     02      |      Odin Thor      |     Asgard      |
+ -----x----- + ---------y--------- + -------z------- +
'''



















