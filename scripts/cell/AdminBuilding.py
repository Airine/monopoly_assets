from KBEDebug import *
from interfaces.Site import Site

"""
当前问题
怎么判断是路过还是踩到，避免重复发放
"""


class AdminBuilding(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 经过正门的人发钱，踩到的翻倍 """
        self.show_send_money(self.curr_player.money_per_round(1))

    def send_money(self):
        """ 只是路过的人发正常金额的钱"""
        self.show_send_money(self.curr_player.money_per_round(1))

    # TODO: 这里调用好像有点问题
    def show_send_money(self, money):
        """ 调用cell 调用客户端显示发放奖学金 """
        self.curr_player.seat.entity.cell.show_send_money(money)




