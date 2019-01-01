from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题
"""


class Stadium(Site):
    def __init__(self, location, room):
        Site.__init__(self, location, room)

    def site_event(self):
        """ 随机事件区 """
        r = random.random()
        if r <= 0.2:  # 800 米获得第一，获得奖金300
            self.curr_player.earn_money(300)
            self.curr_player.seat.entity.cell.random_event(16)
        elif r <= 0.4:  # 运动时不慎拉伤，医疗费200
            self.curr_player.pay_money(200)
            self.curr_player.seat.entity.cell.random_event(17)
        elif r <= 0.6:  # 捡到一张交易卡
            self.curr_player.card_package.buy_immunity(1)
            self.curr_player.seat.entity.cell.random_event(18)
        elif r <= 0.8:  # 步道乐跑代跑，赚了200块
            self.curr_player.earn_money(200)
            self.curr_player.seat.entity.cell.random_event(19)
        elif r <= 1:  # 运动健康身体强壮，获得一张修仙卡
            self.curr_player.card_package.buy_xiuxian(1)
            self.curr_player.seat.entity.cell.random_event(20)



