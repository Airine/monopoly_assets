import KBEngine
from KBEDebug import *
from interfaces.Site import Site
import random

"""
当前问题
1. 需要通过id找到建筑, room 里要有 KBEngine.globalData["Halls"].getRoom(int(self.room_id)).get_site_by_location(location)
这个方法
2. 指定建筑来升级
"""


class Supply(Site):
    def __init__(self, location, room):
        Site.__init__(self, location, room)

    def site_event(self):
        """
        指定建筑破坏，(或者升级)不能是site，只能是自习室或者游戏室
        :return:
        """
        self.curr_player.seat.entity.Next()
        return
        self.curr_player.seat.entity.cell.select_building()

    def select_again(self):
        """ 重新选择建筑, 客户端要同时报错说刚刚那个不是可升级的站点 """
        self.curr_player.seat.entity.cell.select_building_again()

    def destory_building(self, location):
        # 通过id得到建筑
        building = KBEngine.globalData["Halls"].getRoom(int(self.room_id)).get_site_by_location(location)
        # 判断是否可以降级
        if building.update_viable():
            building.downgrade_building()
            # 通过建筑的位置，调用客户端降级动画
            self.curr_player.seat.entity.cell.show_destory_building(building.location)
        else:  # 重新选择一次
            self.select_again()

    def update_building(self, location):
        # 通过id得到建筑
        building = KBEngine.globalData["Halls"].getRoom(int(self.room_id)).get_site_by_location(location)
        # 判断是否可以降级
        if building.update_viable():
            building.update_building()
            # 通过建筑的位置，调用客户端升级动画
            self.curr_player.seat.entity.cell.show_update_building(building.location)
        else:  # 重新选择一次
            self.select_again()
