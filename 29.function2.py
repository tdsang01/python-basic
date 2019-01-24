# positional argument: truyền theo thứ tự
# keyword argument: có thể chỉ định param nào truyền argument nào.
# python có thể cho phép tạo ra các parameter chỉ nhận giá trị bằng việc truyền keyword argument.


def k_team(a, b):
    print(a, b)


k_team(3, b='Free')


def teo(a, b=2, c=3, d=4):  # default value
    f = (a + d) * (b + c)
    print(f)


teo(2)


print('------')


def k2_team(pos_or_key_arg, *, key_arg1, key_arg2):  #  parameter sau * -> keyword only argument(chỉ nhận giá trị theo kiểu keyword argument)
    print(pos_or_key_arg)
    print(key_arg1)
    print(key_arg2)


# k2_team(1, 2, 3)  # TypeError: k2_team() takes 1 positional argument but 3 were given
k2_team(1, key_arg1=2, key_arg2=3)  # -> OK.



