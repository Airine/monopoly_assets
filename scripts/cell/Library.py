from KBEDebug import *
from interfaces.Site import Site

"""
当前问题
"""


class Library(KBEngine.Entity, Site):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Site.__init__(self)

    def site_event(self):
        """ 借阅书籍 """
        self.borrow_book()

    def borrow_book(self):
        """ 每次只能借四本书, 如果上次的没用完就不能继续借 """
        self.curr_player.card_package.add_temp_book_full()
        self.curr_player.seat.entity.cell.show_borrow_book_successful()

