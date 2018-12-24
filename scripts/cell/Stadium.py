from KBEDebug import *
from interfaces.Site import Site

"""
当前问题
"""


class Stadium(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 随机事件区 """
        pass



