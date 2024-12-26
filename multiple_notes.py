### Данный код, создаёт любое количество заметок по введённым данным пользователя
### Каждая заметка хранится в виде словаря в основном списке. Все заметки выводятся в конце программы, в красивом формате
### Код делает проверку корректности ввода на любом этапе и заканчивает свою работу, если юзер вводит слово 'стоп'
import datetime

print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку")

notes = []  ### Основной список в котором хранятся все заметки в виде словарей

while True:

    username = input("Введите имя пользователя: ")
    ### Проверка на пустой ввод
    if len(username.split()) == 0:
        while len(username.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            username = input("Введите имя пользователя: ")

    title = input("Введите заголовок заметки: ")
    ### Проверка на пустой ввод
    if len(title.split()) == 0:
        while len(title.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            title = input("Введите заголовок заметки: ")

    content = input("Введите описание заметки: ")
    ### Проверка на пустой ввод
    if len(content.split()) == 0:
        while len(content.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            content = input("Введите описание заметки: ")

    status = input("Введите статус заметки (например, 'Новая', 'Активна', 'Выполнена'): ")
    ### Проверка на пустой ввод
    if len(status.split()) == 0:
        while len(status.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            status = input("Введите статус заметки (например, 'Новая', 'Активна', 'Выполнена'): ")

    created_date = input("Введите дату создания заметки в формате день-месяц-год: ")
    ### Проверяем формат введённой даты, если пользователь вводит неправильно, конструкция выдаёт ошибку и кидает обратно к началу цикла
    while True:
        try:
            checking_date_format = datetime.datetime.strptime(created_date,
                                                              '%d-%m-%Y')  ### Отдельная переменная для помещения в неё даты в виде класса datetime
        except ValueError:
            print("Вы ввели дату в неправильном формате! Попробуйте ещё раз")
            created_date = input("Введите дату создания заметки в формате день-месяц-год: ")
            continue
        break

    issue_date = input("Введите дату истечения заметки в формате день-месяц-год: ")
    ### Проверяем формат введённой даты, если пользователь вводит неправильно, конструкция выдаёт ошибку и кидает обратно к началу цикла
    while True:
        try:
            checking_date_format = datetime.datetime.strptime(issue_date,
                                                              '%d-%m-%Y')  ### Отдельная переменная для помещения в неё даты в виде класса datetime
        except ValueError:
            print("Вы ввели дату в неправильном формате! Попробуйте ещё раз")
            issue_date = input("Введите дату истечения заметки в формате день-месяц-год: ")
            continue
        break

    format_date = input(
        "В каком формате показывать дату заметки?\n1. День.месяц.год\n2. День.месяц\nВведите только число, '1' или '2': ")
    ###
    if format_date != '1' and format_date != '2':
        while format_date != '1' and format_date != '2':
            print("Вы ввели не тот вариант ответа. Попробуйте ещё раз")
            format_date = input(
                "В каком формате показывать дату заметки?\n1. День.месяц.год\n2. День.месяц\nВведите только число, '1' или '2': ")

    dict_note = {'username': username, 'title': title, 'content': content,
                 'status': status, 'created_date': created_date,
                 'issue_date': issue_date, 'format_date': format_date}

    notes.append(dict_note)  ### Добавляем словарь в наш основной список

    ### Если пользователь, выбирает 'да', то его возвращает к началу цикла, иначе выводим все заметки и заканчиваем цикл
    answer_option = input("Добавить ещё одну заметку? (да/нет): ")
    if answer_option.lower() == 'да':
        continue

    ### Вложенный цикл, который выводит все заметки из списка
    for i in range(0, len(notes)):
        for _ in notes[i]:
            print(f"\nЗаметка №{i + 1}")
            print(f"Имя пользователя: {notes[i]['username']}")
            print(f"Заголовок заметки: {notes[i]['title']}")
            print(f"Описание заметки: {notes[i]['content']}")
            print(f"Статус заметки: {notes[i]['status']}")
            if '1' in notes[i]['format_date']:
                print(f"Дата создания заметки: {notes[i]['created_date'].replace('-', '.')}")
                print(f"Дата истечения заметки: {notes[i]['issue_date'].replace('-', '.')}")
            elif '2' in notes[i]['format_date']:
                print(f"Дата создания заметки: {notes[i]['created_date'][:5:].replace('-', '.')}")
                print(f"Дата истечения заметки: {notes[i]['issue_date'][:5:].replace('-', '.')}")
            break
    break
