'''Зайка — 1'''
a = input()
if 'зайка' in a:
    print('YES')
else:
    print('NO')

'''Музыкальный инструмент'''
a = int(input())
b = int(input())
c = int(input())

if a < (b + c) and b < (c + a) and c < (a + b):
    print('YES')
else:
    print('NO')

'''Властелин Чисел: Две Башни'''
n = int(input())
a = n // 100
# print(a)
b = n // 10 % 10
# print(b)
c = n % 10
# print(c)
min = min(a, b, c)
# print(min)
max = max(a, b, c)
# print(max)
d = (a + b + c) - min - max
# print(d)
if b == 0 and c == 0 or a == b == c:
    print()
elif min == 0:
    print(d, min, " ", max, d, sep=(""))
else:
    print(min, d, " ", max, d, sep=(""))
