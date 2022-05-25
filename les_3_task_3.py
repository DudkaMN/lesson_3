def my_func(i_1, i_2, i_3):
    """Принимает 3 числа и складывает 2 наибольших из них"""
    my_list = [i_1, i_2, i_3]
    my_list.remove(min(my_list))
    print(sum(my_list))


my_func(3, 3, 5)
