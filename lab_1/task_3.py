list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Индекс середины
middle_index = len(list_players) // 2

# Списки первой и второй команд
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
