from funcs import *

def algoritm(mat_1, mat_2, size):
    """
    Выполнение алгоритма задачи 1: сортировка первой матрицы в возрастающем 
    порядке, второй в убывающей, суммирование этих матриц и сортировка этой 
    суммы в убывающем порядке
    :param mat_1: первая матрица
    :param mat_2: вторая матрица
    :param size:  размер матрицы
    """
    
    mat_1 = sort_incr(mat_1, size)
    mat_2 = sort_decr(mat_2, size)
    mat_rezult = sum_arr(mat_1, mat_2, size)
    return sort_decr(mat_rezult, size)

def sum_arr(mat_1, mat_2, size):
    """
    Суммирование матриц
    :param mat_1: первое слагаемое
    :param mat_2: второе слагаемое
    :param size:  размер матриц
    """
    
    mat_rezult = []
    for i in range(size):
        if mat_1[i] == mat_2[i]:
            mat_rezult.append(0)
        else:
            mat_rezult.append(mat_1[i] + mat_2[i])
    return mat_rezult


def menu_first():
    caption_start = "\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (algoritm, False),
        3: (mat_output, False)}
    flag = 1
    print("Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов, первый массив должен быть отсортирован в порядке убывания, второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна нулю. Конечный массив нужно отсортировать в порядке возрастания.")
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        if ch == 1:
            size = input('Введите размер ')
            while is_int(size) != True:
                size = input('Введите целое число ')
            size = int(size)
            mat_1, mat_2 = f(size), f(size)
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            mat_rezult = f(mat_1, mat_2, size)
            flag = 3
        if ch == 3 and valid_comand(ch, flag):
            f(mat_1, mat_2, mat_rezult)
        if is_break:
            break
    return False
    
if __name__ == "__main__":
    menu_first()