'''Таблица умножения'''
s1 = int(input())
for i in range(1, s1 + 1):
    for j in range(i, i * s1 + 1, i):
        print(j, end='')
    print()


number = int(input())
counter_1 = 0
for result in range(number):
    counter_2 = 0
    while (x := input()) != "ВСЁ":
        if x == "зайка" and counter_2 == 0:
            counter_1 += 1
            counter_2 += 1
print(counter_1)