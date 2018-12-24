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

    def move_player(self, steps):
        """客户端调用的时候要告诉我走了几步到的哪里"""
        self.curr_player.change_position(steps)
        # 客户端调用移动动画
        self.curr_player.seat.entity.cell.move_notify(steps)


