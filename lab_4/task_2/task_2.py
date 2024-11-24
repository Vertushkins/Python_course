# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME, encoding='utf-8') as input_file:  # TODO считать содержимое csv файла
        # Считываем из файла с помощью DictReader и преобразуем результат к списку из словарей
        data = list(csv.DictReader(input_file))

    with open(OUTPUT_FILENAME, "w") as output_file:  # TODO Сериализовать в файл с отступами равными 4
        # Записываем список в json файл
        json.dump(data, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
