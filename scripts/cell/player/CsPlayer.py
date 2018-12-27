from player.Player import *

"""计算机系角色"""


class CsPlayer(Player):

    def __init__(self, player_id, room_id, name, seat):
        Player.__init__(self, player_id, room_id, name, seat, "CS")
        self.money = 9000
        self.get_ability_rate = 1.1
        self.card_package = CardPackage(0, 0, 3, 0, 0)  # 三张修仙卡

