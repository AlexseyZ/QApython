'''Раз, два, три! Ёлочка, гори!'''
while input() != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

'''Считалочка'''
a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(i, end=" ")

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

'''Зайка — 3'''

counter = 0
while (x := input()) != 'Приехали!':
    if 'зайка' in x:
        counter += 1
print(counter)

'''Внимание! Акция!'''
summa = 0
while (n := float(input())) != 0:
    if n >= 500:
        s = n - (n * 0.1)
        summa += s
    else:
        summa += n
print(summa)

'''Считалочка 2.0'''

number_start = int(input())
number_end = int(input())

if number_start < number_end:
    for i in range(number_start, number_end + 1):
        print(i, end=' ')
else:
    for i in range(number_start, number_end - 1, -1):
        print(i, end=' ')

'''Излишняя автоматизация 2.0'''
a = input()
b = int(input())
for i in range(b):
    print(a)
