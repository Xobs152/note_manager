### Пример списка с заметками
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]


def save_notes_to_file(notes, filename):
    ### Начинаем вести запись в наш файл, если данного файла не существует, то он создастся
    file = open(filename, 'w', encoding='utf-8')

    ### Записываем в наш файл все заметки из списка в красивом формате с помощью вложенного цикла
    ### В конечном результате в нашем файле будут только заметки из текущего списка
    ### Если в файле были какие-то данные, они удалятся и запишутся заметки
    for i in range(len(notes)):
        for _ in notes[i]:
            file.write(f"Имя пользователя: {notes[i]['username']}\n")
            file.write(f"Заголовок: {notes[i]['title']}\n")
            file.write(f"Описание: {notes[i]['content']}\n")
            file.write(f"Статус: {notes[i]['status']}\n")
            file.write(f"Дата создания: {notes[i]['created_date']}\n")
            file.write(f"Дедлайн: {notes[i]['issue_date']}\n\n")
            break

    ### Закрываем наш файл
    file.close()


save_notes_to_file(notes, "notes.txt")
