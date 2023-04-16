from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа.')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводит результат функции calculate_square_root."""
    if your_number <= 0:
        return ValueError('Число должно быть больше 0')
    sqrt_you_number = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {sqrt_you_number}')


print(message)
calc(25.5)
