
def create_note():
    return print("Заметка успешно создана!")

def  display_notes(notes):
    return print("Ваши заметки:")

def update_note(note):
    return print("Заметки обновлены!")

def delete_note(note):
    return print("Заметка удалена")

def search_notes(notes, keyword=None, status=None):
    return print("Найденные заметки:")

def menu():

    ### Цикл будет продолжаться, пока пользователь не введёт число 6
    ### В данной программе каждая функция не выполняет своего предназначения
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы\n")

        choice = input("Ваш выбор: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            display_notes(2)
        elif choice == '3':
            update_note(3)
        elif choice == '4':
            delete_note(4)
        elif choice == '5':
            search_notes(5)
        elif choice == '6':
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("\nНеверный выбор. Попробуйте снова.")

### Вызываем функцию
menu()
