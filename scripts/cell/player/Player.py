from player.CardPackage import *
from player.Ending import form_ending
SUM_BUILDING_NUM = 24  # 几个格子
GRADUATED_REQUIREMENT = [30, 50, 70, 90]  # 升级和毕业要求达到的学力点
"""
当前问题
"""


class Player:
    def __init__(self, player_id, room_id, name, seat, major):
        self.seat = seat  # 座位
        self.grade = 1  # 当前年级
        self.major = major  # 专业
        self.player_id = player_id  # 玩家id, 1, 2, 3, 4
        self.room_id = room_id  # 房间id
        self.position = 0  # 玩家位置
        self.name = name  # 玩家姓名
        self.money = 3000  # 初始化金钱
        self.ability = 10  # 学历点
        self.administrative_warning = 0  # 行政警告
        self.loop = 1  # 第几圈
        self.study_warning = 0  # 学业警告
        self.card_package = CardPackage(0, 0, 0, 0, 0)  # 道具卡
        self.house = list()  # 所拥有的房间
        self.rest_day = 0  # 休息时间
        self.earn_money_rate = 1  # 收钱比率
        self.get_ability_rate = 1  # 获得学历点率
        self.money_per_round = 1000  # 每回合发的钱数
        self.personality = Personality() # 性格点

    def graduate_grade(self):
        """ 升年级，或者毕业 """
        if self.grade > 4:
            self.graduation()
        elif self.ability > GRADUATED_REQUIREMENT[self.grade]:
            self.grade += 1
            self.seat.entity.cell.show_graduate(self.grade)
            # 不管升没升成功loop都置为0， 开始下一个循环（没升学成功其实已经没机会第一了）
            self.loop = 0

    def graduation(self):
        """ 毕业操作(包括退学死亡的时候也调用)"""
        self.seat.entity.cell.show_graduate(self.evaluate_graduation())

    def evaluate_graduation(self):
        """ 根据点数评估毕业去向， 并且返回结果"""
        return form_ending(self)

    def is_dead(self):
        """ 是否死亡 """
        if self.administrative_warning + self.study_warning >= 3 or self.money <= 0:
            # 退学也是一种毕业
            self.graduation()

    def change_position(self, forward_num):
        """改变位置"""
        if self.position + forward_num > SUM_BUILDING_NUM:
            self.loop += 1
        self.position += forward_num
        if self.position > SUM_BUILDING_NUM:
            self.get_scholarship(1)
        self.position = self.position % SUM_BUILDING_NUM

    def pay_money(self, money_num):
        """付钱"""
        self.money -= money_num

    def earn_money(self, money_num):
        """赚钱"""
        self.money += money_num * self.earn_money_rate

    def get_ability(self, ability):
        """获得学历点"""
        self.ability += ability * self.get_ability_rate

    def loss_ability(self, ability):
        """扣学历点"""
        self.ability -= ability * self.get_ability_rate

    def add_administrative_warnning(self):
        """行政警告一次"""
        self.administrative_warning += 1

    def add_study_warnning(self):
        """学业警告一次"""
        self.administrative_warning += 1

    def set_rest_day(self, rest_day):
        """休息时间"""
        self.rest_day = rest_day

    def rest_one_day(self):
        """ 休息过了一天 """
        self.rest_day -= 1

    def get_scholarship(self, i=1):
        """每回合发钱, 踩到正门发两倍"""
        scholarship = i * self.money_per_round
        self.money += scholarship
        return scholarship

    def buy_house(self, money, house):
        """ 买房子 """
        self.pay_money(money)
        self.house.append(house)

    def sell_house(self, money, house):
        """ 卖房子 """
        self.earn_money(money)
        self.house.pop(house)


class Personality:
    def __init__(self):
        self.real_point = 0
        self.research_point = 0
        self.manage_point = 0
        self.social_point = 0
        self.art_point = 0

    def add_real_point(self, num):
        self.real_point += num

    def add_research_point(self, num):
        self.research_point += num

    def add_manage_point(self, num):
        self.manage_point += num

    def add_social_point(self, num):
        self.social_point += num

    def add_art_point(self, num):
        self.art_point += num

    def sub_real_point(self, num):
        self.real_point -= num

    def sub_research_point(self, num):
        self.research_point -= num

    def sub_manage_point(self, num):
        self.manage_point -= num

    def sub_social_point(self, num):
        self.social_point -= num

    def sub_art_point(self, num):
        self.art_point -= num