import KBEngine
from KBEDebug import *
from interfaces.Site import Site
from interfaces.Building import Building
"""
当前问题
"""


class GameRoom(KBEngine.Entity, Site, Building):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def update_viable(self):
        """判断是否可以升级"""
        return True

    def site_event(self):
        """ 付钱或者扣学力点 """
        # 计算玩家需要付的钱, 如果主人是金融系的是要加钱的
        if self.curr_player.player_id == self.owner.player_id:  # 如果是主人，什么事都没有
            self.curr_is_owner = True
        else:
            if self.curr_player.character.cardpackage.is_hava_immunity():
                # (需要付的钱，减少的学力点，是否有免疫卡)
                self.curr_player.seat.entity.show_enter_game(self.game_pay, self.level, True)
            else:
                # 没卡直接付钱
                self.play_game()

    def play_game(self):
        # 没卡直接付钱
        self.curr_player.player_pay(self.game_pay)
        self.owner.earn_money(self.game_pay)
        self.curr_player.seat.entity.show_playe_game(self.game_pay, self.level, False)

    def player_use_card(self):
        """使用免疫卡"""
        self.curr_player.cardpackage.remove_immunity()

    def try_to_buy(self):
        """ 如果当前玩家有交易卡，且不是主人，尝试去购买此建筑 """
        if self.curr_player.card_package.is_have_transaction() and not self.curr_is_owner:
            self.curr_player.seat.entity.cell.show_weather_to_buy(self.owner, 'GameRoom')

    def show_update(self):
        """ 客户端显示升级, 传入的location位置"""
        self.curr_player.seat.entity.cell.show_building_update(self.location)

    def show_downgrade(self):
        """ 客户端显示降级, 传入的location位置"""
        self.curr_player.seat.entity.cell.show_building_downgrade(self.location)

