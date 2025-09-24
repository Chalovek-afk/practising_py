import math


def gcd(a: int, b: int) -> int: # НОД
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int: # НОК
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def is_prime(n: int) -> bool: # Простое число
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def inverse(n: float) -> float: # Обратное
    if n == 0:
        raise ValueError("Обратное число для 0 не существует.")
    return 1 / n

def sqrt(n: float) -> float: # Корень
    if n < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определён в действительных числах.")
    return math.sqrt(n)