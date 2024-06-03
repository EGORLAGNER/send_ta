from services import generate_dataset

# ТЗ
# отправить пользователям сообщение
# тем, у кого есть email - отправить на email
# у кого нет email, отправить по sms на номер телефона

data = generate_dataset(100)

URL_SITE = 'https://roga_and_kopitas.com'


def notify_users(dataset, url_site):
    count_sent_sms = 0
    count_sent_emails = 0

    for user in dataset:
        name = user.get('name')
        phone = user.get('number')
        email = user.get('email')
        if email == ' ':
            _send_message_by_sms(name, phone, url_site)
            count_sent_sms += 1
            continue
        _send_message_by_email(name, email)
        count_sent_emails += 1
    return count_sent_emails, count_sent_sms


def _send_message_by_email(user_name, email):
    message = (f'Глубоко уважаемый {user_name}, возрадуйтесь! На майские праздники никто не работает. \n'
               f'Не обожритесь шашлыком и не обпейтесь водкой!!! ')
    print(message)
    print(f'сообщение отправлено на почтовый ящик: {email}')
    print()


def _send_message_by_sms(user_name, phone_number, site_url):
    message = (f'Глубоко уважаемый {user_name}, изльвольте проследовать на наш великолепный сайт '
               f'{site_url} для прочтения актуальных, важных новостей')

    print(message)
    print(f'сообщение отправлено на номер: {phone_number}')
    print()


result = notify_users(
    dataset=data,
    url_site=URL_SITE
)

