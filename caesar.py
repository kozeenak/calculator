en = 'abcdefghijklmnopqrstuvwxyz'
ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def caesar(text, shift, mode, lang):
    if lang == 'рус':
        alphabet = ru
    else:
        alphabet = en
    if mode == 'дешифр':
        shift = -shift

    result = ''
    for char in text:
        if char.lower() in alphabet:
            upp = char.isupper()
            index = alphabet.index(char.lower())
            new_index = (index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            result += new_char.upper() if upp else new_char
        else:
            result += char
    print(result)

text = input('Привет, это программа для шифра Цезаря. Введи свою строку для шифровки: ')
shift = int(input('На сколько символов нужно сместить текст? '))
mode = input('Нужно зашифровать или вернуть обратно? шифр/дешифр ')
lang = input('На каком языке нужно? рус/анг ')

caesar(text, shift, mode, lang) 