from funcs import *

def algoritm(m_1, m_2, m_3):
    """
    Проверка, является ли число m_3 суммой m_2 и m_1. Если является, возвращает 
    сумму этих трех чисел, возведенную в степень наименьшего
    :param mat_1: первое слагаемое
    :param mat_2: второе слагаемое
    :param mat_3: сумма 
    """
    
    if m_1+m_2 == m_3:
        degree = sort_decr([m_1, m_2, m_3], 3)[0]
        return (m_1+m_2+m_3)**degree


def menu_second():
    caption_start = "\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (algoritm, False),
        3: (mat_output, False)}
    flag = 1
    print("Входные данные: 3 массива с числами одинакового размера. Нужно проверить, могут ли два числа под одним и тем же номером в сумме давать третье число. Если могут, то сумма трех чисел возводится в степень наименьшего числа.")
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
            mat_1, mat_2, mat_3 = f(size), f(size), f(size)
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            mat_rezult = []
            for i in range(size):
                rezult = f(mat_1[i], mat_2[i], mat_3[i])
                mat_rezult.append(rezult)
            flag = 3
        if ch == 3 and valid_comand(ch, flag):
            f(mat_1, mat_2, mat_rezult, mat_3)
        if is_break:
            break
    return False

if __name__ == "__main__":
    menu_second()