from KBEDebug import *
from interfaces.Site import Site
"""
当前问题
"""

price = {'Immunity': 200, 'Transaction': 100, 'Xiuxian': 100, 'book': 50}

class Lychee(KBEngine.Entity, Site):

    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 卖东西 """
        # 客户端显示商店
        self.curr_player.seat.entity.cell.showShop(self.curr_player.money)

    def buy_product(self, im, tra, xiu, boo):
        """ 客户端选择后调用 """
        if im > 0:
            self.curr_player.card_package.buy_immunity(im)
            self.curr_player.card_package.pay_money(im * price['Immunity'])
        elif tra > 0:
            self.curr_player.card_package.buy_transaction(tra)
            self.curr_player.card_package.pay_money(tra * price['Transaction'])
        elif xiu > 0:
            self.curr_player.card_package.buy_xiuxian(xiu)
            self.curr_player.card_package.pay_money(xiu * price['Xiuxian'])
        elif boo > 0:
            self.curr_player.card_package.buy_book(boo)
            self.curr_player.card_package.pay_money(boo * price['Book'])

