def my_div():
    """Запрашивает два числа,
    возвращает частное от деления.
    обрабатывает ошибку ZeroDivisionError
    """
    try:
        s_1 = int(input("введите первое число: "))
        s_2 = int(input("введите второе число: "))
        return (s_1 / s_2)
    except ZeroDivisionError:
        print('второе число не должно быть равно 0')


div = my_div()
print(div)
