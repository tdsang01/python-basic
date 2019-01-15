a = 9.5
print(a, type(a))
from decimal import *
getcontext().prec = 5
print(Decimal(10)/Decimal(3))
print(type(Decimal(10)/Decimal(3)))

