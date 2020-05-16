from loto_utils import *

def main():
    bag = Bag(MAX_NUMBERS)

    while True:
        players_count = input('Введите количство игроков от 2 до 10')

        try:
            players_count = int(players_count)
            if players_count < 2 or players_count > 10:
                print('Игроков не может быть меньше 2 или больше 10')
            else:
                break
        except:
            print('Введите число от 2 до 10')

    players = []
    players_type = {str(i + 1): Player.players_type[i] for i in range(len(Player.players_type))}

    for i in range(players_count):
        # print('Игрок номер', i+1, '\n' + 'Выбеите тип игрока:')

        while True:
            print('Игрок номер', i + 1, '\n' + 'Выбеите тип игрока:')
            for key in players_type.keys():
                print(key, players_type[key])

            input_player_type = input()

            if input_player_type in players_type.keys():
                player_type = players_type[input_player_type]
                break
            else:
                print('Неверный выбор!')

        player_name = input('Введите имя игрока: \n')

        players.append(Player(player_name, player_type))

    humans_in_game = Player.humans_in_game()
    losse_players = []
    while True:

        while losse_players:
            l_pl = losse_players.pop()
            players.remove(l_pl)

        current_num = bag.chouse_number()
        print('Выбран номер:', current_num, '(Осталось {})'.format(bag.check_number()))

        for n, player in enumerate(players):

            print(player.show_card())

            if player.player_type == 'Компьютер':

                if current_num in player.card.numbers:
                    player.cross_out(current_num)

            elif player.player_type == 'Человек':
                answer = input('Зачеркнуть число? (y,n)')

                if answer == 'y':

                    if player.cross_out(current_num) == -1:
                        print('Игрок {} проиграл!'.format(player.name))
                        losse_players.append(player)
                        humans_in_game -= 1

                        if humans_in_game == 0:
                            print("Все люди проиграли!")
                            exit()

                elif answer == 'n':

                    if player.cross_out(current_num) == -1:
                        pass

                    else:
                        print('Игрок {} проиграл!'.format(player.name))
                        losse_players.append(player)
                        humans_in_game -= 1

                        if humans_in_game == 0:
                            print("Все люди проиграли!")
                            # exit()

            if player.card.num_in_card == 0:
                print('Игрок {} победил!'.format(player.name))
                exit()


main()