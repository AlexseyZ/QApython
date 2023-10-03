'''Азбука'''
n = int(input())
counter = 0

for i in range(n):
    if input()[0] in "абв":
        counter += 1

if counter == n:
    print("YES")
else:
    print("NO")

'''Кручу-верчу'''
s = input()
for i in s:
    print(i, end='\n')

'''А роза упала на лапу Азора 4.0'''
s = str(input())
a = s[::-1]
if s == a:
    print("YES")
else:
    print("NO")

'''Возведение в степень'''
data = list(map(int, input().split()))
number = int(input())
for i in data:
    print(i ** number, end=' ')

'''Анонс новости'''
lg = int(input())
c = int(input())
for i in range(c):
    n = input()
    if len(n) > lg:
        print(n[: lg - 3].ljust(lg, "."))
    else:
        print(n)
