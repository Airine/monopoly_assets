from KBEDebug import *
from interfaces.Site import Site
import random
"""
当前问题
1. 随机事件还没定义完
"""


class Lakeside(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 随机事件区 """
        r = random.randint(0, 5)
        if r == 0:  # 丢失校卡，损失金钱
            lose_money = random.randint(100, 300)
            self.curr_player.pay_money(lose_money)
            self.curr_player.seat.entity.cell.lose_student_card(lose_money)
        elif r == 1:  # 骑滑板车被刘主任追赶，跑不跑
            self.curr_player.seat.entity.cell.see_schoolmaster()
        elif r == 2:  # 看见校长，要不要上去打招呼
            self.curr_player.seat.entity.cell.see_schoolmaster()
        elif r == 3:  # 小组讨论，
            self.curr_player.seat.entity.cell.group_meeting()
        elif r == 4:
            pass
        elif r == 5:
            pass




