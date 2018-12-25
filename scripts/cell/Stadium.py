from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题
"""


class Stadium(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 随机事件区 """
        r = random.random(0, 5)
        if r < 0.2:  # 800 米获得第一，获得奖金300
            pass
        elif r < 0.3:  # 运动时不慎拉伤，医疗费200
            pass
        elif r < 0.5:  # 捡到一张交易卡
            pass
        elif r == 3:  # 步道乐跑，健康值提升
            pass
        elif r == 4:  #
            pass
        elif r == 5:  #
            pass



