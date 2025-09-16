def is_window_fit(height, width, diameter):
    return diameter <= height+2 and diameter <= width+2


a = int(input('Высота форточки: '))
b = int(input('Ширина форточки: '))
d = int(input('Диаметр головы Вовы: '))

print(is_window_fit(a, b, d))
