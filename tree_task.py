from funcs import *

def proverka_once(m_1, m_2, m_3):
    """
    Первичная проверка для симметричных вычислений (от перемены мест 1 и 2 
    элемента ничего не меняется). Сумма и произведение. Возвращает True, если 
    mat_1 и mat_2 дают mat_3
    :param mat_1: первое число
    :param mat_2: второе число
    :param mat_3: результат математических операций над mat_1 и mat_2
    """
    
    if (m_1+m_2 == m_3) or (m_1*m_2 == m_3):
        return True
    else:
        return proverka_twice(m_1, m_2, m_3)

def proverka_twice(m_1, m_2, m_3):
    """
    Вторичная проверка для несимметричных вычислений (деление, корень, разница, 
    возведение в степень). Возвращает True, если mat_1 и mat_2 дают mat_3
    :param mat_1: первое число
    :param mat_2: второе число
    :param mat_3: результат математических операций над mat_1 и mat_2
    """
    
    for i in range(2):
        if m_2 != 0:
            if (m_1/m_2 == m_3) or (m_1**(1/m_2) == m_3):
                return True
        if (m_1-m_2 == m_3) or (m_1**m_2 == m_3):
            return True
        m_1, m_2 = m_2, m_1
    return False
        

def menu_tree():
    caption_start = "\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (proverka_once, False),
        3: (mat_output, False)}
    flag = 1
    print("Входные данные: 3 массива с числами. Требуется проверить, можно ли получить число из 3 массива, арифметическими преобразованиями с числами из двух других массивов. Числа проверяются последовательно (т.е. если проверяется первое число в 3 массиве, в двух других тоже проверяются только первые числа).")
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
    menu_tree()