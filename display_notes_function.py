import datetime

notes = [{'username': 'Алексей', 'title': 'Список дел', 'content': 'Купить продукты на неделю', 'status': 'Новая',
        'created_date': '27-11-2024', 'issue_date': '30-11-2024'}, {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'В процессе',
        'created_date': '25-11-2024', 'issue_date': '01-12-2024'}]

### Функция для показа заметок
def  display_notes(notes):
    ### Мы проверяем с помощью len() размер списка, если len(notes) = 0, то заметок у нас нет
    ### Иначе мы выводим одну или более заметок
    if len(notes) == 0:
        return print("У вас нет сохранённых заметок.")
    else:
        print("Список заметок:")
        for i in range(0, len(notes)):
            for _ in notes[i]:
                print("\n-----------------------------")
                print(f"\nЗаметка №{i + 1}")
                print(f"Имя пользователя: {notes[i]['username']}")
                print(f"Заголовок: {notes[i]['title']}")
                print(f"Описание: {notes[i]['content']}")
                print(f"Статус: {notes[i]['status']}")
                print(f"Дата создания: {notes[i]['created_date']}")
                print(f"Дедлайн: {notes[i]['issue_date']}")
                break
        print("\n-----------------------------")

### Вызываем функцию
display_notes(notes)