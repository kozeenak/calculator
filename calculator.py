def to_decimal(num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = num.upper()
    res = 0
    for i, digit in enumerate(reversed(num)):
        val = digits.index(digit)
        res += val * (base**i)
    return res

def from_decimal(decimal, base):
    if decimal == 0:
        return '0'
    digits = '0123456789ABCDEF'
    res = ''
    while decimal > 0:
        res = digits[decimal % base] + res
        decimal //= base
    return res

def convert(num, base_1, base_2):
    decimal = to_decimal(num, base_1)
    res = from_decimal(decimal, base_2)
    return res

num = input('Привет, это калькулятор систем счисления, какое число вы хотите перевести? ')
base_from = int(input('Из какой системы счисления? '))
base_to = int(input('В какую ситему счисления? '))

print(convert(num, base_from, base_to))