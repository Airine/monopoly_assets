from KBEDebug import *


class Building(object):
    def __init__(self):
        # 初始建筑等级和价钱, 以及每个人需要付的钱
        self.level = 1
        self.price = 50
        self.game_pay = 500
        self.study_pay = 100
        self.owner = None
        self.curr_is_owner = False

    def sell_site(self, older, newer):
        """ 卖房子"""
        if older is not None:  # 不是第一次购买
            newer.cardpackage.remove_transaction()
            # 玩家收钱比率
            self.game_pay /= older.earn_money_rate
            self.study_pay /= older.earn_money_rate
            self.game_pay *= newer.earn_money_rate
            self.study_pay *= newer.earn_money_rate
        newer.buy_house(self.price, self)
        self.owner = newer

    def update_building(self):
        """升级建筑，最多三级, 收钱翻倍"""
        if self.level < 3:
            self.level += 1
            self.price *= 2
            # 自习室加的学力点，或者游戏厅减的学力点翻倍
            self.update_pay()

    def update_pay(self):
        """路过费用升级"""
        self.game_pay *= 2
        self.study_pay *= 2

    def downgrade_building(self):
        """降级建筑"""
        if self.level > 1:
            self.level -= 1
            self.price /= 2
            # 自习室加的学力点，或者游戏厅减的学力点翻倍
            self.downgrade_pay()

    def downgrade_pay(self):
        """费用降级"""
        self.game_pay /= 2
        self.study_pay /= 2