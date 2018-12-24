from KBEDebug import *
from interfaces.Site import Site
import random
"""
当前问题
1. 题库没有发出去
2. 还在确定学力点是怎么加的
"""


class BuildingOne(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 两个事件，随机发生 """
        r = random.random(0, 1)
        if r < 0.7:
            # 进入教室回答问题
            self.quiz()
        else:
            # 选择考试
            self.curr_player.seat.entity.cell.exam()

    def quiz(self):
        # 要发一个题库
        self.curr_player.seat.entity.cell.quiz()

    def exam_choices(self, cheat):
        """客户端做出考试选择后调用"""
        if cheat:  # 作弊
            r = random.random(0, 1)
            if r < 0.3:  # 考试被抓, 学业警告
                self.curr_player.add_study_warnning()
                self.curr_player.seat.entity.cell.show_cheat_warning()  # 客户端显示考试被抓，收到了学业警告
            else:
                # 没被抓，学力点+3
                self.curr_player.get_ability(3)
                self.curr_player.seat.entity.cell.show_get_study_ability(3)  # 客户端显示学力点增加了3
        else:
            self.curr_player.get_ability(1)
            self.curr_player.seat.entity.cell.show_get_study_ability(3)  # 客户端显示学力点增加了1

