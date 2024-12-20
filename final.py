note = []
titles = []

note.append(input("Введите имя пользователя: "))
titles.append(input("Введите первый заголовок заметки: "))
titles.append(input("Введите второй заголовок заметки: "))
titles.append(input("Введите третий заголовок заметки: "))
note.append(titles)
note.append(input("Введите описание заметки: "))
note.append(input("Введите статус заметки (например, 'Активна', 'Выполнена'): "))
note.append(input("Введите дату создания заметки в формате 'день-месяц-год': "))
note.append(input("Введите дату истечения заметки в формате 'день-месяц-год': "))
print(note)
format_date = input(f"В каком формате показывать дату заметки?\n1. {note[4].replace('-', '.')}\n2. {note[4][:5:].replace('-', '.')}\nВведите только число, '1' или '2': ")


print("\nВы ввели следующие данные:")
print("Имя пользователя:", note[0])
print("Заголовки заметки:", note[1])
print("Описание заметки:", note[2])
print("Статус заметки:", note[3])
if '1' in format_date:
    print("Дата создания заметки:", note[4].replace('-', '.'))
    print("Дата истечения заметки:", note[5].replace('-', '.'))
elif '2' in format_date:
    print("Дата создания заметки:", note[4][:5:].replace('-', '.'))
    print("Дата истечения заметки:", note[5][:5:].replace('-', '.'))