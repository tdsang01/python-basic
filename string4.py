a = 'Có gì hot kg'
print(a)
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())

# center: center(5,<fullchar>)
b = a.center(30, '-')
print(b)
# left: ljust()
# right: rjust()

# encode()
c = a.encode(encoding='utf-8', errors='strict')
print(c)

# join()
print(a.join(['1', '2']))

# replace()
print(a.replace('g', 'r', -2))

# strip(str) -> cat cac ky tu 2 dau boi ky tu str
d = a.strip('g')
print(d + '|')
# lstrip(), rstrip()

# split(), rsplit()
splitChar = ' '
e = a.split(splitChar, 2) # no parameter => default is space
print(e)

# partition(), rpartition()
f = a.partition('hot')
print(f)

# count()
count = a.count('g', 0, 6)  # count(char, start, end)
print(count)

# startswith(), enswith()
isStartWith = a.startswith('C')
print(isStartWith)
print(a.startswith('g',3))
print(a.startswith('g',3, 4))

# find(), rfind()
find = a.find('hot')
print(find)

# index() giong find, nhung index() neu tim ko ra thi throw error

# islower(), isupper()

# istitle()

# isdigit()
print('54'.isdigit())

# isspace()