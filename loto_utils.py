import random

MAX_NUMBERS = 90
NUMBERS_IN_CARS = 15

class Bag:
    """
    Класс 'Мешок' для хранения бочонков
    """

    def __init__(self, max_num):
        """
        Инициализируем мешок чисел
        :param max_num: максимальное количесвто чисел
        """
        self.numbers_list = list(range(1, max_num))

    def check_number(self):
        """
        Проверяем сколько чисел в мешке
        :return: количесвто чисел в мешке
        """
        return len(self.numbers_list)

    def __del_number(self, number):
        """
        Удаляем число из мешка
        :param number: число, к-ое удаляем
        """
        self.numbers_list.remove(number)

    def chouse_number(self):
        """
        Вынимае случайное число из мешка
        :return: выбранное число
        """
        number = random.choice(self.numbers_list)
        self.__del_number(number)
        return number

class Card:

    def __init__(self, max_number, number_in_card = NUMBERS_IN_CARS):
        numbers = list(range(1, max_number))
        random.shuffle(numbers)
        self.numbers = numbers[:number_in_card]
        self.numbers.sort()
        self.num_in_card = len(self.numbers)

    def cross_out(self, number):
        if number in self.numbers:
            idx = self.numbers.index(number)
            self.numbers[idx] = '-'
            self.num_in_card -= 1
        else:
            return -1


class Player:

    def __init__(self, name):
        self.name = name
        self.card = Card(MAX_NUMBERS)

    def cross_out(self, number):
        return self.card.cross_out(number)


bag = Bag(MAX_NUMBERS)
player_0 = Player('Игрок')
player_1 = Player('Компьютер')
while True:
    current_num = bag.chouse_number()
    print('Выбран номер:', current_num, '(Осталось {})'.format(bag.check_number()))
    print('Карточка', player_0.name)
    print(player_0.card.numbers)
    print('Карточка', player_1.name)
    print(player_1.card.numbers)
    if current_num in player_1.card.numbers:
        player_1.cross_out(current_num)
    answer = input('Зачеркнуть число? (y,n)')
    if answer == 'y':
        if player_0.cross_out(current_num) == -1:
            print('Вы проиграли!')
            exit()
    elif answer == 'n':
        if player_0.cross_out(current_num) == -1:
            pass
        else:
            print('Вы проиграли!')
            exit()

    if player_0.card.num_in_card == 0:
        print('Победил игрок ', player_0.name)
        exit()

    if player_1.card.num_in_card == 0:
        print('Победил игрок ', player_1.name)
        exit()
