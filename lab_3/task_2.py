# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, spl=','):
    # Конвертируем списки в множества
    first_group_list = first_group.split(spl)
    second_group_list = second_group.split(spl)

    # Находим пересечение множеств и возвращаем его список
    inter = list(set(first_group_list).intersection(second_group_list))
    return inter


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, spl='|'))
