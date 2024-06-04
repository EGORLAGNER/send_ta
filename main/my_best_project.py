import random

from services import generate_dataset

# ТЗ
# отправить пользователям сообщение
# тем, у кого есть email - отправить на email
# у кого нет email, отправить по sms на номер телефона

data = generate_dataset(100)

URL_SITE = 'https://roga_and_kopitas.com'




class Employee:
    """Класс описывающий работника"""

    def __init__(self, name, email_address, phone_number):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name} | {self.email_address} | {self.phone_number}'

    def is_email(self):
        """
        Проверяет, имеется ли у работника email адрес
        :return:
        """
        if not self.email_address:
            return False
        return True


class DataBase:
    def __init__(self):
        self.employees = []

    def __str__(self):
        return 'база данных какого-то предприятия'

    def add_employees(self, employee_list):
        for employee in employee_list:
            if isinstance(employee, Employee):
                self.employees.append(employee)
                print('работник добавлен')
            else:
                print('нефига это не работник')

    def count_employees(self):
        print(f'В базе данных:[{len(self.employees)}] работников')

    def get_random_terpila(self):
        terpila = random.choices(population=self.employees, k=1)
        return f'{print(terpila[0])} - ты работаешь в выходные'


def create_employee_from_dataset(dataset):
    employees = []
    for dictionary in dataset:
        name = dictionary['name']
        email_address = dictionary['email']
        if email_address == ' ':
            email_address = False
        phone_number = dictionary['number']

        employee = Employee(name, email_address, phone_number)
        employees.append(employee)
    return employees


def send_messages_to_employees(employees):
    count_sms = 0
    count_email = 0
    for employee in employees:
        if employee.is_email():
            print(f'Отправить сообщение на email: {employee.email_address} для {employee.name}')
            count_email += 1
        else:
            print(f'Отправить sms сообщение на номер: {employee.phone_number} для {employee.name}')
            count_sms += 1
    print(f'Сообщения отправлены. SMS: {count_sms}, Email: {count_email}')


if __name__ == '__main__':
    employees = create_employee_from_dataset(data)

    names = ['1', '2', '3']

    db = DataBase()
    db.count_employees()
    db.add_employees(employees)
    db.count_employees()
    db.add_employees(names)
    db.count_employees()
    db.get_random_terpila()
