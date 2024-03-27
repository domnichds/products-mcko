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
        new_string = [string[0], string[1], string[2], float(string[3]), float(string[4])] # Перевод численных значений во float
        result.append(new_string)
    return result


products = get_data('products.csv')
summ_total = 0
with open('products_new.csv', 'w') as file:
    file.write('Category;product;Date;Price per unit;Count;Total\n') # Запись шапку таблицы
    for i in range(len(products)):
        product = products[i]
        total = product[3] * product[4]
        if product[0] == 'Закуски':
            summ_total += total
        product.append(total)
        write_string = f'{product[0]};{product[1]};{product[2]};{product[3]};{product[4]};{total};\n'
        file.write(write_string)
print(summ_total)
_ = input() # Пустое поле ввода для более конкретного отображения данных