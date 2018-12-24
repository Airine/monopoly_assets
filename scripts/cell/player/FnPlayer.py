from player.Player import *

"""金融系角色"""


class FnPlayer(Player):

    def __init__(self, player_id, room_id, name, seat):
        Player.__init__(self, player_id, room_id, name, seat, "FN")
        self.money = 5000
        self.earn_money_rate = 1.2
        self.card_package = CardPackage(0, 2, 0, 0, 0)  # 两张交易卡
