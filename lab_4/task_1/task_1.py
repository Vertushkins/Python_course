# TODO решите задачу
import json

def task() -> float:
    filename = "input.json"

    with open(filename) as file:
        data = json.load(file)  # Считываем данные из файла
        # Определяем сумму элементов массива, составленного из произведений score и weight
        result = sum([element["score"] * element["weight"] for element in data])

        return round(result, 3)  # Округляем до 3 знака после запятой и возвращаем

print(task())
