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
        r = random.random(0, 1)
        if r < 0.2:  # 借女朋友钱保健被发现，获得行政警告
            self.curr_player.add_administrative_warnning()
            self.curr_player.show_prostitution()
        elif r < 0.3:  # 在专家公寓学习外语备考托福， 学力点加一, 金钱值减少1000
            pass
        elif r < 0.4:  # 帮忙接待专家，和专家谈笑风生，某种性格点加一
            pass
        elif r < 0.5:  # 捡到一张免疫卡！
            pass
        elif r < 0.6:  # 在教工之家参加活动, 外交值提升
            pass
        elif r < 0.8:  # 参加
            pass
