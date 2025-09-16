def get_root_of_quadratic_equation(a, b, c):
    if not a:
        return 'Ошибка!'
    d = b ** 2 - 4*a*c
    if d < 0:
        return 'Нет рациональных корней!'
    elif d == 0:
        return round(-b / (2*a), 1)
    x1 = round((-b + d ** 0.5) / (2*a), 1)
    x2 = round((-b - d ** 0.5) / (2*a), 1)
    return x1, x2

a = int(input())
b = int(input())
c = int(input())

print(get_root_of_quadratic_equation(a, b, c))
