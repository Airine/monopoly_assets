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
                self.curr_player.seat.entity.show_enter_game(self.game_pay, self.level, 0)
            else:
                # 没有免疫卡
                self.curr_player.seat.entity.show_enter_game(self.game_pay, self.level, 1)

    def play_game(self):
        # 没卡直接付钱
        self.curr_player.player_pay(self.game_pay)
        self.owner.earn_money(self.game_pay)
        self.try_to_buy()

    def player_use_card(self):
        """使用免疫卡"""
        self.curr_player.cardpackage.remove_immunity()
        self.try_to_buy()

    def try_to_buy(self):
        """ 如果当前玩家有交易卡，且不是主人，尝试去购买此建筑 """
        if self.curr_player.card_package.is_have_transaction() and not self.curr_is_owner:
            self.curr_player.seat.entity.cell.show_weather_to_buy(self.owner, self.price)
        else:
            # 结束操作，下一位玩家
            KBEngine.globalData["Halls"].getRoom(int(self.room_id)).next()

    def sell_site(self, older, newer):
        """ 卖房子(玩家第一次建筑的时候也调用)"""
        if older is not None:  # 不是第一次购买
            newer.cardpackage.remove_transaction()
            # 玩家收钱比率
            self.game_pay /= older.earn_money_rate
            self.study_pay /= older.earn_money_rate
            self.game_pay *= newer.earn_money_rate
            self.study_pay *= newer.earn_money_rate
            older.sell_house(2 * self.price, self)
            newer.buy_house(2 * self.price, self)
        else:
            newer.buy_house(self.price, self)
        self.owner = newer
        KBEngine.globalData["Halls"].getRoom(int(self.room_id)).next()

    def show_update(self):
        """ 客户端显示升级, 传入的location位置"""
        self.curr_player.seat.entity.cell.show_building_update(self.location)

    def show_downgrade(self):
        """ 客户端显示降级, 传入的location位置"""
        self.curr_player.seat.entity.cell.show_building_downgrade(self.location)

