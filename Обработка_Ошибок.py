### Конструкция для обработки ошибок
try:
    with open('example.txt') as file:
        print(file.read())
except FileNotFoundError:  ### Если файл не существует, об этом сообщается и создается новый файл
    file = open('example.txt', 'w')
    print('Файл example.txt не найден. Создан новый файл.')
except UnicodeDecodeError:  ### Если в файле используется не поддерживаемая кодировка
    print('Ошибка при чтении файла example.txt. Проверьте его содержимое.')
except PermissionError:  ### Если для работы с файлом не хватает прав
    print('Ошибка при работе с файлом example.txt. Нет прав доступа')
