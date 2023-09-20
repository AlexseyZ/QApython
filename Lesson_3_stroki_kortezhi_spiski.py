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
