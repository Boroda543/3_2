def send_email(message, recipient, sender ="university.heip@gmail.com"):
    if "@" not in sender or "." not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    else:
        print(f"Письмо успешно отправлино с адреса {sender} на адрес {recipient}")
        print(f"НЕСTАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлино с адреса {sender} на адрес {recipient}. ")

send_email('Это сообшение для проверки связи','vasyok13137@gmail.com' )
send_email('Вы видите это сообшение как лутший студент курса!',
           'urban.fan@mail.ru',sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре','urban.teacher@mail.ru',
           sender = 'urban.teacher@mail.ru')

