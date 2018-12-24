
"""
当前问题
1. 医院离开的时候其实不是清空curr_player的，但是好像没有什么影响，新来的人自然会赋值到curr
2. 站点应该有一个属性是room_id
"""


class Site(object):

    def __init__(self):
        self.enter_player_list = list()
        self.curr_player = None

    def enter_site(self, seat):
        """ 进入站点 """
        self.curr_player = seat.character
        if seat.character not in self.enter_player_list:
            self.enter_player_list.append(seat.character)

    def update_viable(self):
        """判断是否可以升级"""
        return False

    def leave_site(self, player_id):
        """ 离开站点 """
        self.enter_player_list.pop(self.find_player_from_list(player_id))
        self.curr_player = None

    def site_event(self):
        """ 站点事件 """
        pass

    def find_player_from_list(self, player_id):
        """ 通过id 找到在list里的玩家"""
        for character in self.enter_player_list:
            if player_id == character.palyer_id:
                return character

