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
        self.curr_player.set_rest_day(2)
        # room 把角色加入休息列表
        if self.curr_player.card_package().is_have_immunity():
            self.curr_player.seat.entity.cell.use_immunity_for_hospital()
        self.curr_player.seat.entity.cell.player_get_rest(2)

    def escape(self, player_id):
        """ 这个很特殊，玩家是之前就到这的，不是curr_player"""
        esc_player = self.find_player_from_list(player_id)
        # 调用动画选择是否花钱逃脱，如果不选择就继续呆着，天数减一
        esc_player.seat.entity.cell.choose_to_escape()

    def use_money_to_escape(self, player_id):
        """ 玩家选择花钱离开"""
        leave_player = self.find_player_from_list(player_id)
        leave_player.pay_money(200)  # 暂定200块
        self.leave_site(player_id)

    def stay_hospital(self, player_id):
        """ 玩家不选择花钱 """
        player = self.find_player_from_list(player_id)
        player.rest_one_day()
        if player.rest_day == 0:
            self.leave_site(player_id)

