# So sánh giữa 2 iterable cùng loại.

# == và is

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)
list3 = list1
print(list3 is list1)

a = -6
b = -6
print('a is b: ', a is b)  # False
# Toán tử "is" chỉ trả về True khi  giá trị trong khoảng -5:256,
# hoặc một số chuỗi có số ký tự dưới 20.

#  NOT, AND, OR

# Chuyển các gái trị về boolean bằng hàm bool()
# Những giá trị khi chuyển về boolean kết quả False: 0, None, Rỗng
