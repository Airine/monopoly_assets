from player.Player import *

"""电子系角色"""


class EePlayer(Player):

    def __init__(self, player_id, room_id, name, seat):
        Player.__init__(self, player_id, room_id, name, seat, "EE")
        self.card_package = CardPackage(0, 0, 0, 3, 0)  # 三张升级卡

