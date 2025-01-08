

notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
          'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
         {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
          'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
         {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
          'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

### Функция для поиска заметок по слову из следующих разделов: username, title, content и/или статусу
def search_notes(notes, keyword=None, status=None):

    ### Если список с заметками пустой, функция возвращает данный вывод и заканчивает свою работу
    if len(notes) == 0:
        return print("Ни одной заметки не найдено.")

    ### В этот список будем записывать индекс словаря из списка заметок для будущего вывода
    index_notes = []

    ### Мы проверяем есть ли keyword в username, title или content и равен ли status статусу заметки
    ### Если оба
    if keyword != None and status != None:
        for i in range(len(notes)):
            if (keyword in notes[i]['username'] or keyword in notes[i]['title'] or keyword in notes[i]['content']) and status == notes[i]['status']:
                index_notes.append(i)
    elif keyword != None:
        for i in range(len(notes)):
            if keyword in notes[i]['username'] or keyword in notes[i]['title'] or keyword in notes[i]['content']:
                index_notes.append(i)
    elif status != None:
        for i in range(len(notes)):
            if status == notes[i]['status']:
                index_notes.append(i)

    ### Если в список index_notes ничего не добавилось, значит введённые данные(keyword и status) не соответствуют ни одной заметки
    ### Значит, если длина index_notes = 0, тогда мы возвращаем соответсвующее сообщение и функция прекращает свою работу
    ### Если длина index_notes > 0, тогда данное условие не выполняется и продолжается работа функции
    if len(index_notes) == 0:
       return print("Заметки, соответствующие запросу, не найдены.")

    ### Цикл для вывода заметки в красивом формате, переменная j используется для номера заметки
    print("Найдены заметки:")
    j = 1
    for i in index_notes:
        print(f"\nЗаметка №{j}:")
        print(f"Имя пользователя: {notes[i]['username']}")
        print(f"Заголовок: {notes[i]['title']}")
        print(f"Описание: {notes[i]['content']}")
        print(f"Статус: {notes[i]['status']}")
        j += 1



search_notes(notes, keyword='работы', status='выполнено')