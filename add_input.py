username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
format_date = input(f"В каком формате показывать дату заметки?\n1. {created_date.replace('-', '.')}\n2. {created_date[:5:].replace('-', '.')}\nВведите только число, например, '1': ")


print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
if '1' in format_date:
    print("Дата создания заметки:", created_date)
    print("Дата истечения заметки:", issue_date)
elif '2' in format_date:
    print("Дата создания заметки:", created_date[:5:].replace('-', '.'))
    print("Дата истечения заметки:", issue_date[:5:].replace('-', '.'))
