def s():
    """суммирует внесенные числа, при обнаружении иного объекта останавливает программу"""
    res = 0
    while True:
        try:
            numbers = list(input('введите числа: ').split(' '))
            for i in (numbers):
                res += int(i)
            print(res)
        except ValueError:
            return (res)
            break


print(s())
