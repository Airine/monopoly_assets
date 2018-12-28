from KBEDebug import *
from interfaces.Site import Site

"""
当前问题
"""


class BusStation(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 调用客户端移动提示选择要移动到哪个位置 """
        self.curr_player.seat.entity.cell.select_position_to_move()

    def move_player(self, site_id):
        """客户端调用的时候要告诉我走到那里"""
        # 通过目的位置计算出移动了多少步
        if self.location <= site_id:
            steps = site_id - self.location
        else:
            steps = 24 - (self.location - site_id)
        self.curr_player.change_position(steps)
        # 客户端调用移动动画
        self.curr_player.seat.entity.cell.move_notify(self.curr_player.seat.seatIndex,steps)



