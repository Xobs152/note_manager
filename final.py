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

dict_note = {'username': note[0], 'titles': note[1], 'content': note[2], 'status': note[3], 'created_date': note[4],
             'issue_date': note[5]}

note.append(input(
    f"В каком формате показывать дату заметки?\n1. {dict_note['created_date'].replace('-', '.')}\n2. {dict_note['issue_date'][:5:].replace('-', '.')}\nВведите только число, '1' или '2': "))

dict_note['format_date'] = note[6]

print("\nВы ввели следующие данные:")
print("Имя пользователя:", dict_note['username'])
print("Заголовки заметки:", dict_note['titles'])
print("Описание заметки:", dict_note['content'])
print("Статус заметки:", dict_note['status'])

if '1' in dict_note['format_date']:
    print("Дата создания заметки:", dict_note['created_date'].replace('-', '.'))
    print("Дата истечения заметки:", dict_note['issue_date'].replace('-', '.'))
elif '2' in dict_note['format_date']:
    print("Дата создания заметки:", dict_note['created_date'][:5:].replace('-', '.'))
    print("Дата истечения заметки:", dict_note['issue_date'][:5:].replace('-', '.'))

