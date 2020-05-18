import random

MAX_NUMBERS = 90
NUMBERS_IN_CARS = 15


def generate_random_seq(max_, count, min_=1, sort_flag=False):
    """
    Генерирует count случайных чисел в
    промежутке от min_ до max_ без повторений
    :param max_: верхний порог чисел
    :param min_: ничжний порог чисел
    :param count: количесвто чисел в последовательности
    :return: список случайных count чисел от min_ до max_ без повторений
    """

    assert max_ - min_ > count, 'Слишком много чисел для промежутка!'

    list_ = list(range(min_, max_ + 1))
    random.shuffle(list_)
    res = list_[:count]
    if sort_flag:
        res.sort()

    return res


class Bag:
    """
    Класс 'Мешок' для хранения бочонков
    """

    def __init__(self, max_num):
        """
        Инициализируем мешок чисел
        :param max_num: максимальное количесвто чисел
        """
        self.numbers_list = list(range(1, max_num+1))

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

    def __str__(self):
        """
        Выводим номера бочонков которые остались в мешке с помощью магического метода str
        Метод вызывается при вызове переменной с объектом класса
        :return: номера бочонков которые остались в мешке
        """
        return self.numbers_list

    def __len__(self):
        """
        Выводим количество бочонков оставшихся в мешке
        :return:
        """
        return self.check_number()

    def __getitem__(self, item):
        return self.numbers_list[item]

    def __eq__(self, other):
        return self.numbers_list == other.numbers_list


class Card:

    def __init__(self,
                 max_number,
                 number_in_card=NUMBERS_IN_CARS,
                 lines_count=3,
                 num_in_line=9):
        self.num_in_line = num_in_line
        self.numbers = generate_random_seq(max_number, number_in_card)
        step = NUMBERS_IN_CARS // lines_count
        self.card_lines = {'line_' + str(i + 1): self.numbers[i * step:(i + 1) * step] for i in range(lines_count)}

        for key in self.card_lines.keys():
            numbers = self.card_lines[key]
            numbers.sort()
            self.card_lines[key] = numbers

        self.lines_position = {
            'line_' + str(i + 1): generate_random_seq(self.num_in_line - 1, 5, min_=0, sort_flag=True) for i in
            range(lines_count)}
        self.numbers.sort()
        self.num_in_card = len(self.numbers)
        self.length_card = 3 * self.num_in_line

    def cross_out(self, number):
        for nums in self.card_lines.values():
            if number in nums:
                idx = nums.index(number)
                nums[idx] = '-'
                self.num_in_card -= 1
                res = None
                break
            else:
                res = -1
        return res

    def prepear_card(self):

        res_str = ''
        for line in self.card_lines.keys():
            nums = self.card_lines[line]
            possition = self.lines_position[line]
            for i in range(self.num_in_line):
                if i in possition:
                    idx = possition.index(i)
                    num = nums[idx]
                    if num != '-':
                        if num < 10:
                            res_str += ' ' + str(num) + ' '
                        else:
                            res_str += str(num) + ' '
                    else:
                        res_str += ' ' + num + ' '
                else:
                    res_str += '   '
            res_str += '\n'

        return res_str

    def __str__(self):
        """
        Сформировываем строку с визуализацией карточки.
        :return: строка с числами на карточке с визуализацией
        """
        res = self.prepear_card()
        return res

    def __len__(self):
        """
        Выводим количество незачеркнутых чисел в карточке
        :return:
        """
        return self.num_in_card

    def __getitem__(self, item):
        if item >= 0:
            if item < 5:
                return self.card_lines['line_1'][item]
            elif item < 10:
                return self.card_lines['line_2'][item-5]
            elif item < 16:
                return self.card_lines['line_3'][item-10]
        else:
            if item > -6:
                return self.card_lines['line_3'][item]
            elif item > -11:
                return self.card_lines['line_2'][item+5]
            elif item > -16:
                return self.card_lines['line_3'][item+10]

    def __eq__(self, other):
        return self.numbers == other.numbers


class Player:
    players_type = ('Человек', 'Компьютер')
    human_players = 0

    def __init__(self, name, player_type):
        self.name = name
        self.card = Card(MAX_NUMBERS)
        self.player_type = player_type
        if self.player_type == 'Человек':
            Player.human_players += 1

    @staticmethod
    def humans_in_game():
        return Player.human_players

    def cross_out(self, number):
        return self.card.cross_out(number)

    def show_card(self):
        # print(self.card.length_card)
        start_count = (self.card.length_card - len(self.name)) // 2
        header = start_count * '-' + self.name + start_count * '-'
        end = '-' * self.card.length_card + '\n'
        res = '\n'.join([header,
                         str(self.card)
                         # self.card.prepear_card()
                         ])
        res += end

        return res

    def __str__(self):
        """
        Выводим информацию о игроке, имя и тип
        :return:
        """
        return ', '.join(['Игрок ' + self.name, self.player_type])

    def __len__(self):
        """
        Возвращаем колчисество незачеркнутых чисел в карточке игрока
        :return:
        """
        return len(self.card)

    def __eq__(self, other):
        return self.name == other.name and self.players_type == other.player_type

# def main():
#     bag = Bag(MAX_NUMBERS)
#
#     while True:
#         players_count = input('Введите количство игроков от 2 до 10')
#
#         try:
#             players_count = int(players_count)
#             if players_count < 2 or players_count > 10:
#                 print('Игроков не может быть меньше 2 или больше 10')
#             else:
#                 break
#         except:
#             print('Введите число от 2 до 10')
#
#     players = []
#     players_type = {str(i + 1): Player.players_type[i] for i in range(len(Player.players_type))}
#
#     for i in range(players_count):
#         # print('Игрок номер', i+1, '\n' + 'Выбеите тип игрока:')
#
#         while True:
#             print('Игрок номер', i + 1, '\n' + 'Выбеите тип игрока:')
#             for key in players_type.keys():
#                 print(key, players_type[key])
#
#             input_player_type = input()
#
#             if input_player_type in players_type.keys():
#                 player_type = players_type[input_player_type]
#                 break
#             else:
#                 print('Неверный выбор!')
#
#         player_name = input('Введите имя игрока: \n')
#
#         players.append(Player(player_name, player_type))
#
#     humans_in_game = Player.humans_in_game()
#     losse_players = []
#     while True:
#
#         while losse_players:
#             l_pl = losse_players.pop()
#             players.remove(l_pl)
#
#         current_num = bag.chouse_number()
#         print('Выбран номер:', current_num, '(Осталось {})'.format(bag.check_number()))
#
#         for n, player in enumerate(players):
#
#             print(player.show_card())
#
#             if player.player_type == 'Компьютер':
#
#                 if current_num in player.card.numbers:
#                     player.cross_out(current_num)
#
#             elif player.player_type == 'Человек':
#                 answer = input('Зачеркнуть число? (y,n)')
#
#                 if answer == 'y':
#
#                     if player.cross_out(current_num) == -1:
#                         print('Игрок {} проиграл!'.format(player.name))
#                         losse_players.append(player)
#                         humans_in_game -= 1
#
#                         if humans_in_game == 0:
#                             print("Все люди проиграли!")
#                             exit()
#
#                 elif answer == 'n':
#
#                     if player.cross_out(current_num) == -1:
#                         pass
#
#                     else:
#                         print('Игрок {} проиграл!'.format(player.name))
#                         losse_players.append(player)
#                         humans_in_game -= 1
#
#                         if humans_in_game == 0:
#                             print("Все люди проиграли!")
#                             # exit()
#
#             if player.card.num_in_card == 0:
#                 print('Игрок {} победил!'.format(player.name))
#                 exit()
#
#
# main()