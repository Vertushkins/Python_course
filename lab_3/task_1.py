# TODO Напишите функцию для поиска индекса товара

def find_first_index(list_, find_item):
    for index, item in enumerate(list_):  # Перебираем все индексы и элементы списка
        if item == find_item:  # Если находим нужный элемент, то возвращаем его индекс
            return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, find_item)  # TODO Вызовите функцию, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
