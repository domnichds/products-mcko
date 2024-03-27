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


def get_promocode(string):
    """
    Функция принимает строку таблицы и генерирует промокод для товара в этой строке

    Описание аргументов:
    string - список, содержащий елементы строки таблицы
    """
    for i in range(len(string)): # Цикл для перевода всех значений в строки
        string[i] = str(string[i])
    promo = f'{string[1][0] + string[1][1]}{string[2][0] + string[2][1]}{string[1][-1] + string[1][-2]}{string[2][4] + string[2][3]}'
    return promo.upper()


products = get_data('products.csv')
with open('products_promo.csv', 'w') as file:
    file.write('Category;product;Date;Price per unit;Count;Promocode;\n')
    for i in range(len(products)):
        string = products[i]
        string.append(get_promocode(string))
        write_string = f'{string[0]};{string[1]};{string[2]};{string[3]};{string[4]};{string[5]};\n'
        file.write(write_string)
