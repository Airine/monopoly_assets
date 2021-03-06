from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题
"""


class Canteen(Site):
    def __init__(self, location, room):
        Site.__init__(self, location, room)

    def site_event(self):
        """ 食堂，随机事件区 """
        r = random.random()
        INFO_MSG(self.curr_player)
        INFO_MSG(self.curr_player.money)
        if r < 0.3:  # 吃到欣园食堂食物中毒，获得赔偿200块
            self.curr_player.earn_money(200)
            self.curr_player.seat.entity.cell.random_event(11)
            INFO_MSG("pei chang")
        elif r < 0.5:  # 吃了一次火锅，幸福美满但什么事情都没有发生
            self.curr_player.seat.entity.cell.random_event(12)
            INFO_MSG("huo guo")
        elif r < 0.6:  # 在食堂排队错过上课，学力点扣1
            self.curr_player.loss_ability(1)
            self.curr_player.seat.entity.cell.random_event(13)
            INFO_MSG("pai dui")
        elif r < 0.8:  # 受不了食堂点了外卖，金钱减100
            self.curr_player.pay_money(100)
            self.curr_player.seat.entity.cell.random_event(14)
            INFO_MSG("wai mai")
        else:  # 补充能量，获得修仙卡一张
            self.curr_player.card_package.buy_xiuxian(1)
            self.curr_player.seat.entity.cell.random_event(15)
            INFO_MSG("xiu xianka")
        INFO_MSG(self.curr_player)
        INFO_MSG(self.curr_player.money)




