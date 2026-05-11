import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
num = int(input('Это генератор паролей. Сколько паролей нужно сделать? '))
lenPw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? ')
if digOn == 'да':
    chars += digits
if ABCon == 'да':
    chars += uppercase_letters
if abcOn == 'да':
    chars += lowercase_letters
if chOn == 'да':
    chars += punctuation
if excOn == 'да':
    for c in 'il1Lo0O':
        chars.replace(c, '')

def generate_password(lenght, chars):
    password = ''
    for j in range(lenght):
        password += random.choice(chars)
    print(password)

for j in range(1, num + 1):
    print('Пароль номер', j)
    generate_password(lenPw, chars)