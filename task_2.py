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



def alphabet_sort(list):
    """
    Функция принимает список и сортирует его в алфавитном порядке

    Описание аргументов
    list - список для сортировки
    """
    for i in range(1, len(list)):
        el = list[i]
        j = i
        while j > 0 and list[j][0] < list[j - 1][0]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
        list[j] = el
    return list


products_sort = alphabet_sort(get_data('products.csv'))
mv_category = products_sort[0][0]
ma_lst = []
ma_price = 0
for string in products_sort:
    if string[0] == mv_category and string[3] > ma_price:
        ma_price = string[3]
        ma_lst = string
print(f'В категории: {mv_category} самый дорогой товар: {ma_lst[1]} его цена за единицу товара составляет {ma_lst[3]}')
_ = input() # Пустое поле ввода для более конкретного отображение данных