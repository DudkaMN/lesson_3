def int_func(text):
    """проверяет введено ли слово строчными латинскими буквами"""
    for i in text:
        if 'a' <= i <= 'z':
            continue
        else:
            return False
            break
    return True

phrase = input('введите фразу строчными латинскими буквами: ').split()
if(int_func(phrase)) == True:
    print(str(' '.join(phrase)).title())
else:
    print("ошибка,введите слово строчными латинскими буквами")