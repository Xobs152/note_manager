### Данный код позволяет удалять любую заметку по заголовку или имени пользователя и выводит оставшиеся
### Когда заметок не остается, программ говорит об этом и завершает свою работу
### Если юзер вводит неправильные данные, то его об этом уведомляют и кидает к началу цикла

### Текущие заметки
notes = [{'username': 'Алексей', 'title': 'Список продуктов', 'content': 'купить продукты на неделю', 'status': 'Новая',
          'created_date': '12-12-1212', 'issue_date': '12-12-1212', 'format_date': '2'},
         {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'Активна',
          'created_date': '12-12-1212', 'issue_date': '12-12-1212', 'format_date': '1'}]

### Цикл, выводящий первые три пункта заметки
for i in range(0, len(notes)):
    for _ in notes[i]:
        print(f"\nЗаметка №{i + 1}")
        print(f"Имя пользователя: {notes[i]['username']}")
        print(f"Заголовок заметки: {notes[i]['title']}")
        print(f"Описание заметки: {notes[i]['content']}")
        break

while True:

    ### Переменная для сохранения длины списка
    len_notes = len(notes)

    ### Цикл удаляет весь словарь с заметкой по её названию или имени пользователя
    deleting_note = input("\nВведите имя пользователя или заголовок для удаления заметки: ")
    for j in range(0, len(notes)):
        if deleting_note.lower() == notes[j]['username'].lower() or deleting_note.lower() == notes[j]['title'].lower():
            notes.pop(j)
            break
    ### Если длина списка равна нулю, значит пользователь удалил все заметки, программа уведомляет об этом и заканчивает свою работу
    if len(notes) == 0:
        print("Успешно удалено. Заметок больше не осталось.")
        break

    ### Если длина списка не изменилась после цикла, значит пользователь ввёл не те данные, и его возвращает с началу
    ### Если длина списка изменилась, значит что-то удалилось и это условие код пропустит
    if len(notes) == len_notes:
        print("Заметок с таким именем пользователя или заголовком не найдены. Попробуйте снова")
        continue

    print("Успешно удалено. Остались следующие заметки:")
    ### ### Цикл, выводящий первые три пункта заметки
    for i in range(0, len(notes)):
        for _ in notes[i]:
            print(f"\nЗаметка №{i + 1}")
            print(f"Имя пользователя: {notes[i]['username']}")
            print(f"Заголовок заметки: {notes[i]['title']}")
            print(f"Описание заметки: {notes[i]['content']}")
            break

    ### Если пользователь вводит что-то помимо 'да' или 'нет', программа уведомляет его об этом и переспрашивает, пока не будет введён правильный вариант ответа
    ### Если пользователь вводит 'да', то программа возвращает его обратно к началу цикла
    ### Если пользователь вводит 'нет', то программа заканчивает свою работу
    answer_option = input("\nУдалить ещё одну заметку? (да/нет): ")
    while answer_option.lower() != 'да' and answer_option.lower() != 'нет':
        answer_option = input("Введите корректные данные. Удалить ещё одну заметку? (да/нет): ")
    if answer_option.lower() == 'да':
        continue
    elif answer_option.lower() == 'нет':
        break

    break
