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
