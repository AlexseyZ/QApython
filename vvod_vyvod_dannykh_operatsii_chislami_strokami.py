'''Привет, всем!'''
n = input()
print('Как Вас зовут?')
print(f"Привет, {n}")

'''Сдача'''
money = int(input())
price = 38 * 2.5
change = int(money - price)
print(change)

'''Магазин'''
price = int(input())
weight = int(input())
money = int(input())
change = int(money - (price * weight))
print(change)

'''Делу — время, потехе — час'''
n = int(input())  # кол-во строк
print("Купи слона!\n" * n)

'''Наказание'''
n = int(input())
c = input()
print(f'Я больше никогда не буду писать "{c}"!\n' * n)

'''Деловая колбаса'''
n = int(input())
x = int(input())
t = 2  # время в минутах, за которое съедает 1 ребенок 1 кусок колбасы

print(int(n / t * x))

'''Детский сад — штаны на лямках'''
name = input()
number = int(input())
last = number % 10  # последняя цифра
fist = number // 100  # первая цифра
med = (number % 100) // 10  # вторая цифра

print(f"Группа №{fist}.\n{last}. {name}.\nШкафчик: {number}.\nКроватка: {med}.")

'''В ожидании доставки'''
h = int(input())
m = int(input())
delivery_time = int(input())
hours = (h + (m + delivery_time) // 60) % 24
minutes = (m + delivery_time) % 60
print(f"{hours // 10}{hours % 10}:{minutes // 10}{minutes % 10}")
