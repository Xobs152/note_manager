import datetime

### Пример словаря с заметкой
note = {'username': 'Алексей', 'title': 'Список дел', 'content': 'Купить продукты на неделю', 'status': 'новая',
        'created_date': '27-11-2024', 'issue_date': '30-11-2024'}


### Функция
def update_note(note):
    ### Цикл проверяет корректность введенных данных
    ### Если пользователь вводит что-то не из списка(username, title, content, status, issue_date) или вводит с ошибкой
    ### Программа уведомляет его об этом, и переспрашивает
    while True:
        ### Переменная: данные для обновления. Содержит в себе ключ из словаря
        data_to_update = input(
            '\nКакие данные вы хотите обновить? Введите одно из списка (username, title, content, status, issue_date): ')
        if data_to_update not in note:
            print("\nВы ввели некорректные данные для обновления заметки. Попробуйте снова")
            continue
        break

    ### Если пользователь вводит issue_date, начнёт выполняться данный блок кода с циклом на проверку корректности введённой даты
    if data_to_update == 'issue_date':
        issue_date = input("Введите новое значение для issue_date: ")
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

            ### Если пользователь ввёл дату в формате день/месяц/год, меняем '/' на '-', чтобы все даты выводились в одном формате
            issue_date = issue_date.replace('/', '-')

            ### Меняем дату дедлайна и возвращаем словарь с обновленной датой
            note['issue_date'] = issue_date
            return print("Заметка обновлена:\n", note)

    print("Введите новое значение для", data_to_update + ":", end=" ")
    ### Переменная: обновлённое значение. Содержит в себе новое значение
    updated_value = input()

    ### Проверка на пустой ввод
    if len(updated_value.split()) == 0:
        while len(updated_value.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            print("Введите новое значение для", data_to_update + ":", end=" ")
            updated_value = input()

    ### Меняем старое значение на новое по ключу, введённому ранее
    ### note[ключ(data_to_update)] = значение(updated_value)
    note[data_to_update] = updated_value
    return print("Заметка обновлена:\n", note)


### Вызываем функцию
update_note(note)

while True:
    answer_option = input("\nЖелаете обновить что-то ещё? (да/нет): ")

    ### Если пользователь вводит что-то помимо да/нет, то его закидывает в цикл
    ### Цикл продолжится пока пользователь не введёт либо 'да', либо 'нет'
    if answer_option != 'да' and answer_option != 'нет':
        while answer_option.lower() != 'да' and answer_option.lower() != 'нет':
            print("\nВы ввели некорректные данные. Попробуйте снова\n")
            answer_option = input("Желаете обновить что-то ещё? (да/нет): ")

    ### Если пользователь вводит 'да', мы вызываем функцию ещё раз, можно обновлять данные сколько захотим
    ### Если пользователь вводит 'нет', мы заканчиваем выполнение программы
    if answer_option.lower() == 'да':
        update_note(note)
    else:
        break
