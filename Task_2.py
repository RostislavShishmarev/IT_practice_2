from Task_1 import get_data


def insert_sort(list_, key=lambda x: x):
    """
    Функция для сортировки вставками
    :param list_: исходный список
    :param key: ключ для сортировки
    :return: None
    """
    for i, el in enumerate(list_):
        if i == 0:
            continue
        j = i - 1
        while key(list_[j]) > key(el) and 0 <= j:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = el


def get_winners(n, class_):
    """
    Возвращает информацию о победителях класса
    :param n: количество победителей
    :param class_: класс
    :return: список строк с информацией
    """
    data = [row for row in get_data() if row['class'].startswith(str(class_))]

    insert_sort(data, key=lambda row: -row['score'])

    result = []
    for i, row in enumerate(data[:n]):
        family, name, father = row["Name"].split()
        result.append(f'{i + 1} место: {name[0]}. {family}')
    return result


if __name__ == '__main__':
    print('10 класс:', *get_winners(3, 10), sep='\n')
