from KBEDebug import *
from interfaces.Site import Site
"""
当前问题
"""

price = {'Immunity': 200, 'Transaction': 100, 'Xiuxian': 100, 'book': 50}


class Lychee(Site):
    def __init__(self, location, room):
        Site.__init__(self, location, room)

    def site_event(self):
        """ 卖东西 """
        # 客户端显示商店
        self.curr_player.seat.entity.cell.show_shop(self.curr_player.money)

    def buy_product(self, im, tra, xiu, boo):
        """ 客户端选择后调用 """
        if im > 0:
            self.curr_player.card_package.buy_immunity(im)
            self.curr_player.pay_money(im * price['Immunity'])
        if tra > 0:
            self.curr_player.card_package.buy_transaction(tra)
            self.curr_player.pay_money(tra * price['Transaction'])
        if xiu > 0:
            self.curr_player.card_package.buy_xiuxian(xiu)
            self.curr_player.pay_money(xiu * price['Xiuxian'])
        if boo > 0:
            self.curr_player.card_package.buy_book(boo)
            self.curr_player.pay_money(boo * price['Book'])
        # 结束操作，下一位玩家
