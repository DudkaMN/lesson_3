def my_func(x, y):
    """
    Возводит число x в степень y.

    Именованные параметры:
    x -- действительное положительное число
    y -- целое отрицательное число

    """
    result = 1
    for i in range(abs(y)):
        result = result * 1 / x
    print(result)


my_func(1.25, -4)
