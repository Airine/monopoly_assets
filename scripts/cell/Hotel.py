import KBEngine
from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题

"""


class Hotel(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 专家公寓发生事件"""
        pass

