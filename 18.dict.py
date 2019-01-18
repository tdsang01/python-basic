# phuong thuc
# copy()
print('---copy()---')
d1 = {'team': 'KTeam', ('h',1): 69}
print(d1) # {'team': 'KTeam', ('h', 1): 69}
d2 = d1.copy()
print(d2)# {'team': 'KTeam', ('h', 1): 69}

# clear
print('---clear()---')
d1.clear()
print(d1)
print(d2)

# get() # tra ve None neu key ko ton tai
print('---get()---')
value = d2.get('team', 'Default value')
print(value) # KTeam
value = d2.get('team1', 'Default value')
print(value) # Default value

# item()
print('---items()---')
item = d2.items()
print(item) # dict_items([('team', 'KTeam'), (('h', 1), 69)])
value = list(item)
print('list: ', value)
print(value[0][0])

# keys(), values()
print('---keys(), values()---')
keys = d2.keys()
values = d2.values()
print('keys: ', keys)
print('values: ', values)

# pop(key) # bo di phan tu key va tra ve gia tri cua key do
# Neu key ko ton tai se throw error neu ko truyen gia tri default
print('---pop()---')
value = d2.pop('team')
print(value) # KTeam
#print(d2.pop('dddd')) # error
print(d2.pop('dddd', 'default value')) # default value

# popitem()
 
# setdefault('WhatsUpGuys') # Neu co key thi tra ve value, neu ko co ky thi them 1 cap key:value ('WhatsUpGuys': None)
# setdefault('WhatsUpGuys', 'Hey') key:value ('WhatsUpGuys': 'Hey')

# update() # cap nhat noi dung

































