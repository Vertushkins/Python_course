numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
skipped_number_index = 4  # Задаем индекс пропущенного элемента

# Вычисляем сумму всех элементов до пропуска и после
sum_of_numbers = sum(numbers[:skipped_number_index]) + sum(numbers[skipped_number_index+1:])
# Вычисляем длину всего списка
length = len(numbers)

# Находим среднее арифметическое и записываем его в пропущенный элемент
average = sum_of_numbers / length
numbers[skipped_number_index] = average

print("Измененный список:", numbers)
