import math


def Prov(string):
    global number
    try:
        number = float(string)
        return number
    except Exception:
        number = Prov(input('Введите число: '))
        return number


def Menu():
    print('''Меню:
    - квадрат
    - круг
    - треугольник
    ''')


def Square(choice):
    global result
    if choice == 'квадрат':
        a = Prov(input('Введите сторону квадрата: '))
        result = a ** 2
    elif choice == 'круг':
        R = Prov(input('Введите радиус: '))
        result = math.pi * R ** 2
    elif choice == 'треугольник':
        type_t = int(input('''Какой у вас тругольник?:
        1 - прямоугольный
        2 - равносторонний
        3 - равнобедренный
        4 - обычный
        '''))
        if type_t == 1:
            a = Prov(input('Введите первый катет: '))
            b = Prov(input('Введите второй катет: '))
            result = a * b / 2
        elif type_t == 2:
            a = Prov(input('Введите сторону треугольника: '))
            result = (a ** 2 * math.sqrt(3)) / 4
        elif type_t == 3:
            a = Prov(input('Введите сторону: '))
            h = Prov(input('Введите высоту: '))
            result = 0.5 * a * h
        elif type_t == 4:
            a = Prov(input('Введите первую сторону треугольника: '))
            b = Prov(input('Введите вторую сторону треугольника: '))
            c = Prov(input('Введите третью сторону треугольника: '))
            p = (a + b + c) / 2
            result = math.sqrt(int(p * (p - a) * (p - b) * (p - c)))
    return int(result)


Menu()
choice = input('Ваш выбор: ')
print(f'Площадь равна: {Square(choice)}')
