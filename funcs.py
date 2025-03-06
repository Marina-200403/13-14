from random import randint

def valid_value(message_input: str, message_err: str, template: list):
    """
    Ввод допустимого целого числа
    :param message_input: Сообщение перед вводом
    :param message_err:   Сообщение при вводе символа, не из шаблона
    :param template:      Список допустимых значений
    :return: целое число
    """
    
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def valid_comand(ch, flag):
    """
    Ввод допустимой команды
    """
    
    if flag >= ch:
        return True
    print ('ERROR')
    return False

def is_int(s):
    """
    Проверка, является ли число s целым
    """
    
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False
    
def input_arr(size):
    """
    Ввод матрицы
    :param size: размер создаваемой матрицы
    """
    
    mat = []
    i = 0
    print ("Введите числа")
    while i != size:
        count = input()
        if is_int(count):
            mat.append(int(count))
            i += 1
        else:
            print ('try again')
    return mat

def generation_arr(size):
    """
    Генерация матрицы
    :param size: размер создаваемой матрицы
    """
    
    mat = []
    for i in range(size):
        mat.append(randint(-10, 10))
    return mat


def sort_incr(mat, size):
    """
    Сортировка матрицы в возрастающем порядке
    :param mat:  сортируемая матрица   
    :param size: размер матриц
    """
    
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]<mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

def sort_decr(mat, size):
    """
    Сортировка матрицы в убывающем порядке
    :param mat:  сортируемая матрица   
    :param size: размер матриц
    """
    
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]>mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

def mat_output(mat_1, mat_2, mat_rezult, mat_3 = []):
    """
    Вывод матриц
    :param mat_1:      первая введенная матрица 
    :param mat_2:      вторая введенная матрица 
    :param mat_rezult: результат выполнения алгоритма
    :param mat_3:      третья введенная матрица, если таковая есть
    :param size:       размер матриц
    """
    
    print(mat_1, '\n', mat_2, '\n', mat_3)
    print(mat_rezult)
    


def make_mat(size):
    """
    Выбор способа создания матрицы - самостоятельный ввод или генерация
    :param size: размер матрицы
    """
    
    i = input('Нажмите Enter, если хотите ввести матрицу ')
    if i == '':
        mat_1 = input_arr(size)
    else:
        mat_1 = generation_arr(size)
    return mat_1

    
    
    