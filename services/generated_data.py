from faker import Faker

fake = Faker("ru_RU")


# print(fake.name())  # Генерирует случайное имя
# print(fake.email())  # Генерирует случайный адрес электронной почты
# print(fake.address())  # Генерирует случайный адрес
def _cleaning_phone_numbers(number):
    """
    Очищает номер.
    Удаляет все символы и пробелы кроме цифр
    :return: очищенный номер
    """
    return number \
        .replace('+7', '8') \
        .replace('(', '') \
        .replace(')', '') \
        .replace(' ', '') \
        .replace('-', '')


def _check_len_number_phone(number):
    """
    Проверяет длину номера телефона.
    Возбуждает исключение если длинна менее или более 11 символов
    :param number:
    :return: ничего не возвращает явным образом
    """
    if not len(number) == 11:
        raise Exception(f'количество цифр в номере: {number}  - {len(number)}, а должно быть ровно 11')


def _generate_phone_numbers(count):
    """
    Генерирует случайным образом телефонные номера
    :param count: количество номеров
    :return: список с номерами
    """

    numbers = []
    for _ in range(0, count):
        number = fake.phone_number()
        clean_number = _cleaning_phone_numbers(number)
        _check_len_number_phone(clean_number)
        numbers.append(clean_number)
    return numbers


def _generate_names(count):
    """
    Генерирует случайные имена
    :param count: количество имен
    :return: список с именами
    """
    names = []
    for _ in range(0, count):
        name = fake.name()
        names.append(name)
    return names


def _generate_emails(count):
    """
    Генерирует случайные email адреса
    :param count: количество адресов
    :return: список с адресами
    """
    emails = []
    for _ in range(0, count):
        email = fake.email()
        emails.append(email)
    return emails


def generate_dataset(count):
    """
    Генерирует набор данных.
    Набор данных представляет собой список со словарями,
    которые содержат данные о человеке(полное имя, номер телефона, email адрес)
    :param count:
    :return: список со словарями
    """
    names = _generate_names(count)
    emails = _generate_emails(count)
    numbers = _generate_phone_numbers(count)

    dataset = []

    for index in range(0, count):
        name = names[index]
        email = emails[index]
        number = numbers[index]
        dataset.append({'name': name, 'email': email, 'number': number})
    return dataset



