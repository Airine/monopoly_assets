from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题
"""


class Canteen(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 食堂，随机事件区 """
        r = random.randint(0, 5)
        if r == 0:
            pass
        elif r == 1:
            pass
        elif r == 2:
            pass
        elif r == 3:
            pass
        elif r == 4:
            pass
        else:
            pass




