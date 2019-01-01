import KBEngine
from KBEDebug import *
from interfaces.Site import Site

"""
当前问题
"""


class Hospital(Site):
    def __init__(self, location, room):
        Site.__init__(self, location, room)

    def site_event(self):
        """ 玩家休息两天 """
        # room 把角色加入休息列表
        if self.curr_player.card_package.is_have_immunity():
            self.curr_player.seat.entity.cell.get_rest_in_hospital(2, 1)
        self.curr_player.seat.entity.cell.get_rest_in_hospital(2, 0)
        # self.room.cell.next()

    def escape(self):
        """ 使用免疫卡逃脱 """
        self.curr_player.card_package.remove_immunity()

    def stay_hospital(self):
        """ 玩家呆着 """
        self.curr_player.set_rest_day(2)
        INFO_MSG("Hospital stay")
