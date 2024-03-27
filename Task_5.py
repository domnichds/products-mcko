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


def past_sort(list, key):
    """
    Функция принимает список и списков и сортирует его по значению с индексом key

    Описание аргументов
    list - список для сортировки
    key - индекс, по которому походит сортировка
    """
    for i in range(1, len(list)):
        el = list[i]
        j = i
        while j > 0 and list[j][key] < list[j - 1][key]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
        list[j] = el
    return list


products = get_data('products.csv')
table_hash = {} # Словарь
for string in products:
    if string[0] in list(table_hash.keys()):
        table_hash[string[0]] = table_hash[string[0]] + int(string[4])
    else:
        table_hash[string[0]] = int(string[4])
list_table_hash = []
for name in table_hash.keys():  # Цикл для перевода значений из словоря в список (необходимо для последующей сортировки)
    list_table_hash.append([name, table_hash[name]])
list_table_hash = past_sort(list_table_hash, 1)
for i in range(10): # Цикл для вывода первых 10 значений списка list_table_hash
    print(f'{list_table_hash[i][0]}, {list_table_hash[i][1]}')
_ = input() # Пустое поле ввода для более конкретного отображения данных