new_notes = [
    {
        "username": "Мария",

        "title": "План работы",

        "content": "Подготовить отчёт",

        "status": "в процессе",

        "created_date": "27-11-2024",

        "issue_date": "28-11-2024"
    }
]


### Функция для добавления заметок в файл
def save_notes_to_file(notes, filename):
    ### Начинаем вести запись в наш файл, если данного файла не существует, то он создастся
    file = open(filename, 'a', encoding='utf-8')

    ### Записываем в наш файл все заметки из списка в красивом формате с помощью вложенного цикла
    ### В конечном результате в наш файл добавятся заметки из текущего списка
    ### Если в файле были какие-то данные к ним добавятся наши заметки
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


### Вызываем функцию
save_notes_to_file(new_notes, "notes.txt")
