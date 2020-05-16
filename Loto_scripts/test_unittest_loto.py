import unittest
from loto_utils import *


class TestLoto(unittest.TestCase):

    def test_gen_random_s(self):
        seq = generate_random_seq(90, 15)
        self.assertEqual(len(set(seq)) - len(seq), 0)

    def test_Bag_init(self):
        bag = Bag(90)
        self.assertListEqual(bag.numbers_list, list(range(1, 90 + 1)))

    def test_Bag_check_number(self):
        bag = Bag(90)
        self.assertEqual(bag.check_number(), 90)

    def test_Bag_chouse_number(self):
        bag = Bag(90)
        chosen_num = bag.chouse_number()
        self.assertFalse(chosen_num in bag.numbers_list)

    def test_Card_init(self):
        bag = Bag(90)
        card = Card(90)
        # проверку через множества исопльзовать только если списки без уникальных значений
        self.assertTrue(set(card.numbers).issubset(bag.numbers_list))
        self.assertEqual(card.num_in_card, 15, msg='Неверный параметр кличества чисел в карточке')
        self.assertEqual(card.num_in_line, 9, msg='Неверный параметр количества чисел в строке')

    def test_Card_cross_out(self):
        card = Card(90)
        self.assertEqual(card.cross_out(100), -1)
        num = 25
        if num in card.numbers:
            self.assertEqual(card.cross_out(num), None)
        else:
            self.assertEqual(card.cross_out(num), -1)

    def test_Card_prepear_card(self):
        card = Card(90)
        card.card_lines = {'line_1': [1,2,3,4,5],
                           'line_2': [6,7,8,9,10],
                           'line_3': [11,12,13,14,15]
                           }
        card.lines_position = {'line_1': [0, 2, 4, 6, 8],
                           'line_2': [1, 3, 5, 7, 8],
                           'line_3': [0, 2, 4, 6, 8]
                           }
        str_ = """ 1     2     3     4     5 
    6     7     8     9 10 
11    12    13    14    15 
"""
        print(str)
        self.assertEqual(str_, card.prepear_card())

    def test_Player_human_init(self):
        human_player = Player('Bob', 'Человек')
        self.assertEqual(human_player.name, 'Bob')
        self.assertEqual(human_player.player_type, 'Человек')
        self.assertEqual(Player.human_players, 2)

    def test_Player_comp_init(self):
        human_player = Player('Dag', 'Компьютер')
        self.assertEqual(human_player.name, 'Dag')
        self.assertEqual(human_player.player_type, 'Компьютер')


    def test_Player_cross_out(self):
        human_player = Player('Bob', 'Человек')
        self.assertEqual(human_player.cross_out(100), -1)
        num = 25
        if num in human_player.card.numbers:
            self.assertEqual(human_player.cross_out(num), None)
        else:
            self.assertEqual(human_player.cross_out(num), -1)