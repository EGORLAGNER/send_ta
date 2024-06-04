class Person:
    def __init__(self, f_name, l_name, age, email, phone_number):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def get_info(self):
        print(f'{self.f_name} {self.l_name}')


# data_for_person = ('egor', 'lagner', 32, 'lagner@gmail.com', 89802637247)
#
# dict_data_person = {
#     'f_name': 'egor',
#     'l_name': 'lagner',
#     'age': '32',
#     'email': 'lagner@gmail.com',
#     'phone_number': 89802637247


data_person = ('egor', 'lagner', '32', 'lagner@gmail.com', 89802637247)

person = Person(*data_person)
