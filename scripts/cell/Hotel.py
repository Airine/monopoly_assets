import KBEngine
from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题

"""


class Hotel(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 专家公寓发生事件"""
        r = random.random()
        if r < 0.2:  # 借女朋友钱保健被发现，获得行政警告
            self.curr_player.add_administrative_warnning()
            self.curr_player.seat.entity.cell.random_event(6)
        elif r < 0.3:  # 在专家公寓学习外语备考托福， 学力点加一, 金钱值减少1000
            self.curr_player.get_ability(1)
            self.curr_player.pay_money(1000)
            self.curr_player.seat.entity.cell.random_event(7)
        elif r < 0.4:  # 帮忙接待专家，和专家谈笑风生，research能力加一
            self.curr_player.personality.add_research_point(1)
            self.curr_player.seat.entity.cell.random_event(8)
        elif r < 0.5:  # 捡到一张免疫卡！
            self.curr_player.card_package.buy_immunity(1)
            self.curr_player.seat.entity.cell.random_event(9)
        elif r < 0.6:  # 在教工之家参加活动, 外交值提升
            self.curr_player.personality.add_social_point(1)
            self.curr_player.seat.entity.cell.random_event(10)

