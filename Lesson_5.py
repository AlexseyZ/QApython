'''Символическая выжимка'''
x = input()
y = set(x)
print(''.join(y))

'''Символическая разница'''
a = set(input())
b = set(input())
c = a & b
print(''.join(c))

'''Зайка — 8'''
objects = []
for _ in range(int(input())):
    objects.extend(input().split())
print('\n'.join(set(objects)))