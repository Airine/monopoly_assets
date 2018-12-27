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
        self.quiz_num = 0
        self.quiz_answer = 0

    def site_event(self):
        """ 两个事件，随机发生 """
        r = random.random()
        if r < 0.7:
            # 进入教室回答问题
            self.set_quiz()
            self.curr_player.seat.entity.cell.quiz(self.quiz_num)
        else:
            # 选择考试
            self.curr_player.seat.entity.cell.select_event(6, 57)

    def select_event_callback(self, select):
        """ 客户端回调 """
        if select == 1:
            self.cheat_success()
        elif select ==2:
            self.not_cheat()
        elif select ==3:
            self.cheat_fail()

    def check_answer(self, answer):
        """ 客户端调用，检查是否做对quiz"""
        if answer == self.quiz_answer:
            self.curr_player.get_ability(1)

    def set_quiz(self):
        """ 根据角色获得当前quiz号和答案"""
        answer = [1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1]
        if self.curr_player.major == "CS":
            self.quiz_num = random.randint(1, 5)
        elif self.curr_player.major == "EE":
            self.quiz_num = random.randint(6, 10)
        elif self.curr_player.major == "MA":
            self.quiz_num = random.randint(11, 15)
        elif self.curr_player.major == "FN":
            self.quiz_num = random.randint(16, 20)
        self.quiz_answer = answer[self.quiz_num-1]

    def cheat_success(self):
        self.curr_player.get_ability(3)

    def cheat_fail(self):
        self.curr_player.add_study_warnning()

    def not_cheat(self):
        self.curr_player.get_ability(1)
