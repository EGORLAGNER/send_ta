class Domain:
    """
    Участок земли.
    На нём находится дом, огороды, заборы, гараж, парковочные места.
    """

    def __init__(self):
        self.home = None

    def __str__(self):
        return 'участок земли'

    def add_home(self, home):
        if isinstance(home, Home):
            self.home = home
            print('участку земли добавлен дом')
            return
        print(f'вы пытаетесь добавить на участок не дом, а объект: {home}')
        return


class Home:
    def __init__(self):
        self.users = []

    def __str__(self):
        return 'Дом'

    def add_users(self, users):
        """
        Добавляет новых пользователей
        :param users: список с пользователями
        :return:
        """
        self.users.extend(users)
        print(f'В дом добавлены новые жильцы, в количестве: {len(users)}')

    def get_user_by_name(self, name):
        """
        Возвращает пользователя (или пользователей если их имена совпадают)
        :param name: имя пользователя
        :return: список с пользователями или пользователя
        """
        user_list = []
        for user in self.users:
            if user.name == name:
                user_list.append(user)
        if len(user_list) == 1:
            return user_list[0]
        else:
            return user_list


class BaseCreature:
    """
    Базовый класс для всех живых существ.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} | {self.age} лет'

    def move(self):
        print(f'{self.name} двигается')

    def eat(self):
        print(f'{self.name} ест')

    def sleep(self):
        print(f'{self.name} спит')


class User(BaseCreature):
    def speak(self):
        print(f'{self.name} говорит')


class Dog(BaseCreature):
    def bark(self):
        print(f'{self.name} лает')


class Cat(BaseCreature):
    def mew(self):
        print(f'{self.name} мяукает')


if __name__ == '__main__':
    domain = Domain()
    home = Home()
    user_t = User('Татьяна', 30)
    user_o = User('Ольга', 55)
    user_s = User('Александр', 28)
    user_tt = User('Татьяна', 31)
    dog = Dog('Лавр', 5)

    domain.add_home(home)
    domain.home.add_users([user_s, user_o, user_t, dog, user_tt])
    user = domain.home.get_user_by_name('Александр')
    user.name = 'Вениамин'

    # dog = Dog('Лавр', 5)
    # cat = Cat('Лиса', 1)
    #
    # user_t.move()
    # cat.move()
    # dog.move()
