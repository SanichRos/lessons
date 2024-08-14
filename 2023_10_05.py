def send_email(message , recipient , sender = "university.help@gmail.com"):
    list_domen_search = [".com",".ru",".net"]
    stop_recipient = 1
    stop_sender = 1
    for domen_search in list_domen_search:
        if domen_search in recipient:
            stop_recipient = 0
        if domen_search in sender:
            stop_sender = 0
    if '@' not in recipient  or '@' not in sender or stop_recipient == 1 or stop_sender == 1:
        print("Невозможно отправить письмо с адреса <"+sender+"> на адрес <"+recipient+">")
    elif sender in recipient:
        print("Нельзя отправить письмо самому себе!")
    elif 'university.help@gmail.com' in sender:
        print("Письмо успешно отправлено с адреса <"+sender+"> на адрес <"+recipient+">.")
    else:
        print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <"+sender+"> на адрес <"+recipient+">.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')