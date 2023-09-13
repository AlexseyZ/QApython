'''Делу — время, потехе — час'''
n = int(input())  # кол-во строк
print("Купи слона!\n" * n)

'''В ожидании доставки'''
h = int(input())
m = int(input())
delivery_time = int(input())
hours = (h + (m + delivery_time) // 60) % 24
minutes = (m + delivery_time) % 60
print(f"{hours // 10}{hours % 10}:{minutes // 10}{minutes % 10}")

'''Наше развлечение не осталось незамеченным...'''
n = int(input())
c = input()
print(f'Я больше никогда не буду писать "{c}"!\n' * n)

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

'''Факториал'''
a = int(input())
c = 1
for i in range(1, a + 1):
    # print(i)
    c *= i
print(c)

'''Цифровая сумма'''
n = int(input())
s = 0

while n > 0:
    s += n % 10
    n = n // 10
print(s)

'''Таблица умножения'''
s1 = int(input())
for i in range(1, s1 + 1):
    for j in range(i, i * s1 + 1, i):
        print(j, end='')
    print()
