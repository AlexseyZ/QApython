'''Функциональное приветствие'''
def print_hello(name):
    print(f'Hello, {name}!')


'''Функциональный НОД'''
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        return (a + b)
print(gcd(4, 8))


