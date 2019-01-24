# packing & unpacking argument.

# unpacking argument

print('# unpacking argument')


def k1_team(k, t, e, r):
    print(k)
    print(t, e)
    print('end', r)


lst = ['123', 'hello', 1]  # lst thiếu thì có thể truyền thêm, nhưng thừa thì bị lỗi.

k1_team(*lst, 'four_param')  # Dict chỉ pass được key


# packing argument. => gói các biến lại thành 1 tuple.
def k2_team(*args):
    print(args)
    print(type(args))


print('# packing argument')
k2_team(1, 2, 3)
k2_team(*(x for x in range(5)))  # => unpacking sau do packing


# Nếu sau packing parameter còn các parameter khác, thì các parameter đó phải là keyword argument.
def k3_team(*args, p1):
    print(args)
    print(p1)


print('---k3_team---')
k3_team(*(x for x in range(5)), p1='p1')


def k4_team(p1, *args, p2):
    print(p1)
    print(args)
    print(p2)


print('---k4_team---')
k4_team(1, (1, 2), p2=3)


#  Unpacking arguments vs ** Chú ý: Tên biến (parameter) khi khai báo ở hàm phải giống với key của dict
def k5_team(name, member):
    print(name)
    print(member)


dic = {'name': 'Std', 'member': 696}
print('---k5_team---')
k5_team(**dic)


#  Packing argument với ** Phải truyền argument theo dạng keyword argument.
def k6_team(**kwargs):
    print(kwargs)
    print(type(kwargs))  # => <class 'dict'>
    for key, value in kwargs.items():
        print(key, '->', value)


print('---k6_team---')
k6_team(name=1, member=2)


#  best_function_ever(*args, **kwargs):
def best_function_ever(*args, **kwargs):
    print(args, kwargs)


best_function_ever()


def test(a, **args):
    print(args)
    print(a)
