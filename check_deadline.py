import datetime  ### Используем библиотеку, чтобы возвращать текущую дату

current_date = datetime.datetime.now()  ###

while True:
    ### Проверяем формат введённой даты, если пользователь вводит неправильно, конструкция выдаёт ошибку и кидает обратно к началу цикла
    try:
        date = input("Введите дату дедлайна в формате день-месяц-год: ")
        issue_date = datetime.datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        print("Вы ввели дату в неправильном формате! Попробуйте ещё раз\n")
        continue

    ### Проверка дедлайна в настоящем, прошлом и будущем соответственно
    if issue_date.date() == current_date.date():
        print("Ваш дедлайн истекает сегодня!")
    elif issue_date.date() < current_date.date():
        print("Ваш дедлайн истёк!")
    else:
        print("Количество оставшихся дней до дедлайна:", (issue_date.date() - current_date.date()).days)
    break
