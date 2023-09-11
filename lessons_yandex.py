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
