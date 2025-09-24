def convert_from_10_to_n(num: int, target_numsys: int) -> str:
    if not (2 <= target_numsys <= 16):
        raise ValueError('Значение вне допустимого диапазона')

    if num == 0:
        return str(num)

    digits = "0123456789ABCDEF"
    result = ''
    while num > 0:
        remainder = num % target_numsys
        result = digits[remainder] + result
        num //= target_numsys

    return result


def convert_from_n_to_10(num: str | int, base_numsys) -> str:
    if not (2 <= base_numsys <= 16):
        raise ValueError('Значение вне допустимого диапазона')

    num = str(num)
    if num == '0':
        return num

    digits = "0123456789ABCDEF"
    num_str = num.upper()
    result = 0

    for char in num_str:
        if char not in digits[:base_numsys]:
            raise ValueError(f"Недопустимый символ '{char}' для системы счисления с основанием {base_numsys}")
        digit_value = digits.index(char)
        result = result * base_numsys + digit_value

    return result


print(convert_from_10_to_n(255, 16))
print(convert_from_n_to_10('ff', 16))
