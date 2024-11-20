# TODO Найдите количество книг, которое можно разместить на дискете

memory_capacity = 1.44 * 1024 * 1024  # Объем дискеты в байтах
count_of_pages = 100  # Количество страниц
count_of_strings = 50  # Количество строк
count_of_symbols = 25  # Количество символов
size_of_symbol = 4  # Размер одного символа в памяти в байтах

# Считаем сколько книг поместиться на дискете
count_of_books = int(memory_capacity // (count_of_pages * count_of_strings * count_of_symbols * size_of_symbol))

print("Количество книг, помещающихся на дискету:", count_of_books)
