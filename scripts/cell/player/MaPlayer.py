import random

from player.Player import *

"""数学系角色"""


class MaPlayer(Player):

    def __init__(self, player_id, room_id, name, seat):
        Player.__init__(self, player_id, room_id, name, seat, "MA")
        self.ability = 20
        self.money_per_round = 800
        self.card_package = CardPackage(2, 0, 0, 0, 0)  # 两张免疫卡

    def change_position(self, forward_num):
        if random.random() < 0.2:
            self.money += forward_num * 10
        self.position += forward_num
        self.position = self.position % SUM_BUILDING_NUM
