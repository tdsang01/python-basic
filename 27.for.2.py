# For advance
print('---range()---')
k = range(3)
print(k, type(k))
print(k[1])

print(list(range(2, 5)))  # [2, 3, 4]
print(list(range(10, 3, -2)))  # [10, 8, 6, 4]

# Dùng hàm range() để duyệt vòng lặp for: list, tuple, string,... (có indexing)
lst = ['start', 1, 3, 5, 'hello, how are you?', {'abc', 'xyz'}, {'name': 'STD'}]
for i in range(len(lst)):
    print(lst[i])

# Comprehension
print('---Comprehension---')
a = 'HOW'
b = '--'
c = 'you'
# print(a.capitalize())  # How
print(b.join(a))  # H--O--W
print(b.join((a, c)))  # HOW--you

lst = ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EducaTION'), ('chia', 'se', 'FreE')]]
print(lst)

lst1 = {key: value + 1 for key, value in (('how', 55), ('are', 80), ('you', 45)) if value % 2 != 0}
print(lst1)

# Enumerate # list ko có index -> dùng enumerate để có index.
# enumerate(iterable [, start])
print('---Enumerate---')
student_list = ['Name1', 'Name2', 'Name3', 'Name4']
gen = enumerate(student_list, 5)
print(gen, type(gen))  # <enumerate object at 0x7f6b49d72ca8> <class 'enumerate'>
print(list(gen))  # [(5, 'Name1'), (6, 'Name2'), (7, 'Name3'), (8, 'Name4')]

