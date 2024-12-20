username = input("Введите имя пользователя: ")
title_1 = input("Введите первый заголовок заметки: ")
title_2 = input("Введите второй заголовок заметки: ")
title_3 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
format_date = input(f"В каком формате показывать дату заметки?\n1. {created_date.replace('-', '.')}\n2. {created_date[:5:].replace('-', '.')}\nВведите только число, '1' или '2': ")

titles = [title_1, title_2, title_3]

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
if '1' in format_date:
    print("Дата создания заметки:", created_date)
    print("Дата истечения заметки:", issue_date)
elif '2' in format_date:
    print("Дата создания заметки:", created_date[:5:].replace('-', '.'))
    print("Дата истечения заметки:", issue_date[:5:].replace('-', '.'))