"""
道具卡包
免疫卡：免疫惩罚
交易卡：购买对方建筑
修仙卡：学习时获得学力点*2
升级卡：升级建筑必须使用
书籍：购买来的书籍，每次自习必须使用一本
借来的书籍：图书馆借来的书籍，每次到图书馆可以借四本，下一次四本没用完也只能补到四本
"""


class CardPackage:

    def __init__(self, imm, tra, xiu, book, borr_book):
        self.card_dict = {'Immunity': imm, 'Transaction': tra, 'Xiuxian': xiu,
                          'Book': book, 'Temp_book': borr_book}
        self.size = imm + tra + xiu +  book + borr_book

    def buy_immunity(self, n):
        """添加一张免疫卡"""
        self.card_dict['Immunity'] += n
        self.size += n

    def buy_transaction(self, n):
        """添加一张交易卡"""
        self.card_dict['Transaction'] += n
        self.size += n

    def buy_xiuxian(self, n):
        """添加一张修仙卡"""
        self.card_dict['Xiuxian'] += n
        self.size += n

    def buy_book(self, n):
        """添加一张书籍卡"""
        self.card_dict['Book'] += n
        self.size += n

    def add_temp_book_full(self):
        """图书馆借书，借满到4本"""
        left = self.card_dict['Temp_book']
        self.card_dict['Temp_book'] = 4
        self.size += (4 - left)

    def remove_immunity(self):
        """删除一张免疫卡"""
        if self.is_have_immunity():
            self.card_dict['Immunity'] -= 1
            self.size -= 1

    def remove_transaction(self):
        """删除一张交易卡"""
        if self.is_have_transaction():
            self.card_dict['Transaction'] -= 1
            self.size -= 1

    def remove_xiuxian(self):
        """删除一张修仙卡"""
        if self.is_have_xiuxian():
            self.card_dict['Xiuxian'] -= 1
            self.size -= 1

    def remove_book(self):
        """删除一张书籍卡, 优先移除图书馆借来的书"""
        if self.is_have_book():
            if self.card_dict['Temp_book'] >= 0:
                self.card_dict['Temp_book'] -= 1
            elif self.card_dict['Book'] >= 0:
                self.card_dict['Book'] -= 1
            self.size -= 1

    def is_have_immunity(self):
        return True if self.card_dict['Immunity'] > 0 else False

    def is_have_transaction(self):
        return True if self.card_dict['Transaction'] > 0 else False

    def is_have_xiuxian(self):
        return True if self.card_dict['Xiuxian'] > 0 else False

    def is_have_book(self):
        return True if self.card_dict['Book'] > 0 or self.card_dict['Temp_book'] > 0 else False
