import csv

FIELDNAMES = ['id', 'Name', 'titleProject_id', 'class', 'score']


def get_data():
    """
    Возвращает список словарей с полями таблицы
    :return: список словарей
    """
    with open('students.csv', encoding='utf-8') as file:
        data = list(csv.DictReader(file, delimiter=','))

    for i, row in enumerate(data):
        for key in ['id', 'titleProject_id', 'score']:
            try:
                data[i][key] = int(row[key])
            except ValueError:
                data[i][key] = None
    return data


def get_mark_by_name(name):
    """
    Возвращает информацию о проекте по имени автора
    :param name: имя автора
    :return: строка с информацией
    """
    data = get_data()

    for row in data:
        if row['Name'].startswith(name):
            return f'Ты получил: {row["score"]}, за проект - {row["titleProject_id"]}'


def set_average_score_on_none():
    """
    Задаёт среднюю оценку по классу вместо None и сохраняет в `student_new.csv`
    :return: None
    """
    data = get_data()

    classes = {}
    for i, row in enumerate(data):
        class_ = row['class']
        if class_ in classes:
            if row['score'] is not None:
                classes[class_]['sum'] += row['score']
                classes[class_]['n'] += 1
            else:
                classes[class_]['need'].append(i)
        else:
            sum_, n, need = row['score'], 1, []
            if row['score'] is None:
                sum_, n, need = 0, 0, [i, ]
            classes[class_] = {
                'sum': sum_,
                'n': n,
                'need': need,
            }

    for class_, class_data in classes.items():
        average = round(class_data['sum'] / class_data['n'], 3)
        for i in class_data['need']:
            data[i]['score'] = average

    with open('student_new.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    print(get_data())
    print(get_mark_by_name('Хадаров Владимир'))
    set_average_score_on_none()
