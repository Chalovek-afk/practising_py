def get_VVP(c: int, i: int, g: int, ex: int, im: int) -> int:
    return c + i + g + ex - im


NAME_LST = ['c', 'i', 'g', 'ex', 'im']

value_lst = []
value_dict = {}

for i in NAME_LST:
    value = int(input(f'Введите значение {i}: '))
    value_lst.append(value)
    value_dict[i] = value

print(get_VVP(*value_lst))
print(get_VVP(**value_dict))