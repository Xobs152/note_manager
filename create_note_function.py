### Данная функция позволяет создать заметку, с проверкой корректности введённой даты

import datetime

def create_note():

    ### Ввод описания заметки и проверка на пустую строку
    username = input("\nВведите описание заметки: ")
    ### Проверка на пустой ввод
    if len(username.split()) == 0:
        while len(username.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            username = input("Введите описание заметки: ")

    ### Ввод описания заметки и проверка на пустую строку
    title = input("\nВведите описание заметки: ")
    ### Проверка на пустой ввод
    if len(title.split()) == 0:
        while len(title.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            title = input("Введите описание заметки: ")

    ### Ввод описания заметки и проверка на пустую строку
    content = input("\nВведите описание заметки: ")
    ### Проверка на пустой ввод
    if len(content.split()) == 0:
        while len(content.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            content = input("Введите описание заметки: ")

    ### Ввод статуса заметки и проверка на пустую строку
    status = input("\nВведите статус заметки (например, 'Новая', 'Активна', 'Выполнена'): ")
    ### Проверка на пустой ввод
    if len(status.split()) == 0:
        while len(status.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            status = input("Введите статус заметки (например, 'Новая', 'Активна', 'Выполнена'): ")

    created_date = datetime.datetime.now() ### Возвращаем текущую дату

    issue_date = input("Введите дату дедлайна (день-месяц-год): ")

    ### Проверка корректности введённой даты с помощью цикла и конструкции try-except
    ### Данный блок кода позволяет обработать два варианта введённой даты, день-месяц-год и день/месяц/год
    while True:
        try:
            date = datetime.datetime.strptime(issue_date, '%d-%m-%Y')
        except ValueError:
            try:
                date = datetime.datetime.strptime(issue_date, '%d/%m/%Y')
            except ValueError:
                issue_date = input(
                    "\nВы ввели дату в неправильном формате. Попробуйте ещё раз\nВведите дату дедлайна (день-месяц-год): ")
                continue
        break

    ### Если пользователь ввёл дату в формате день/месяц/год, меняем '/' на '-', чтобы все даты выводились в одном формате
    issue_date = issue_date.replace('/', '-')

    dict_note = {'username': username, 'titles': title, 'content': content, 'status': status,
                 'created_date': created_date.strftime("%d-%m-%Y"),
                 'issue_date': issue_date}

    return print("\nЗаметка создана:", dict_note) ### Функция возвращает вывод словаря

create_note() ### Вызываем функцию