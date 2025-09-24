from romanify import roman2arabic, arabic2roman


arabic = int(input('Введите арабское число: '))
roman = input('Введите римское число: ')

try:
    roman = roman2arabic(roman)
except ValueError:
    raise

print('Сумма:', arabic + roman, arabic2roman(arabic + roman), sep='\n')
print('Разность:', arabic - roman, arabic2roman(arabic - roman), sep='\n')
print('Произведение:', arabic * roman, arabic2roman(arabic * roman), sep='\n')
print('Частное:', arabic // roman, arabic2roman(arabic // roman), sep='\n')

