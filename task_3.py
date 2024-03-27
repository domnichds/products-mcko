import codecs


def get_data(file_name):
    """
    Функция читает файл и преобразует данные в нем, изменяю тип данных некоторых столбцов (цена и количество)
    Возвращается список из списков преобразованных данных

    Описание аргументов:
    file_name - имя читаемого файла
    """
    file = codecs.open(file_name, 'r', 'utf-8-sig')
    array = [el.split(';') for el in file.readlines()]
    result = []
    for string in array[1:]:
        new_string = [string[0], string[1], string[2], float(string[3]), float(string[4])]
        result.append(new_string)
    return result


flag = True
products = get_data('products.csv')
while flag:
    mi = 10 ** 10
    mi_string = []
    user = input('Введите категорию: ')
    if user == 'молоко':
        flag = False
    else:
        for string in products:
            if string[0] == user and mi > string[4]:
                mi = string[4]
                mi_string = string
    if flag:
        if len(mi_string) != 0:
            print(f'В категории: {mi_string[0]} товар: {mi_string[1]} был куплен {int(mi_string[4])} раз')
        else:
            print('Такой категории не существует в нашей БД')
