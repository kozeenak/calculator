import random

num = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку!')
count_attempts = 0


def is_valid(num):
    if 1 <= int(num) <= 100:
        return True
    else:
        return False


while True:
    response = input('Введите число от 1 до 100: ')
    if not is_valid(response):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        response = int(response)

    if response < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count_attempts += 1
    elif response > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count_attempts += 1
    else:
        print('Вы угадали, поздравляем!')
        count_attempts += 1
        break
print('Спасибо, что играли в числовую угадайку. Потрачено попыток:', count_attempts)