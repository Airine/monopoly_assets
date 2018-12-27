import KBEngine
from KBEDebug import *
from interfaces.Site import Site

"""
当前问题
1. 主循环要判断玩家是否在休息，如果在休息,直接调用escape方法
2. 所以在加入休息的时候要获得房间，加入休息列表，或者主函数通过休息天数来判断
"""


class Hospital(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 玩家休息两天 """
        DEBUG_MSG('rest 2 days')
        self.curr_player.set_rest_day(2)
        # room 把角色加入休息列表
        if self.curr_player.card_package.is_have_immunity():
            self.curr_player.seat.entity.cell.get_rest_in_hospital(2, 1)
        self.curr_player.seat.entity.cell.get_rest_in_hospital(2, 0)
        self.room.cell.next()

    def escape(self):
        """ 使用免疫卡逃脱 """
        self.curr_player.card_package.remove_immunity()

    def stay_hospital(self):
        """ 玩家呆着 """
        self.curr_player.set_rest_day()

