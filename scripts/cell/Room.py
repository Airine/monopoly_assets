import random
import time
from player.CsPlayer import CsPlayer
from player.PlayerFactory import PlayerFactory
from AdminBuilding import AdminBuilding
from Library import Library
from BuildingOne import BuildingOne
from Canteen import Canteen
from Lakeside import Lakeside
from Lychee import Lychee
from Supply import Supply
from BusStation import BusStation
from Stadium import Stadium
from Hospital import Hospital
from Hotel import Hotel
from StudyRoom import StudyRoom
from GameRoom import GameRoom

from KBEDebug import *

MAIN_TIMER = 1
ROOM_MAX_PLAYER = 2


class Room(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        KBEngine.addSpaceGeometryMapping(self.spaceID, None, "spaces/mjRoom")
        KBEngine.globalData["Room_%i" % self.spaceID] = self
        print("Change scene")
        self.roomInfo = roomInfo(self.roomKey, self.playerMaxCount)
        # self.room_master = self.EnterPlayerList[0]
        # self.clearPublicRoomInfo()
        self.game = GameController(self.roomInfo, self.playerMaxCount)
        self.site_list = [None]*24
        self.loop = 25
        self._create_site()

    def _create_site(self):
        site_id = 0
        self.site_list[site_id] = AdminBuilding(site_id, self)
        site_id = 3
        self.site_list[site_id] = Library(site_id, self)
        site_id = 6
        self.site_list[site_id] = BuildingOne(site_id, self)
        site_id = 8
        self.site_list[site_id] = Canteen(site_id, self)
        site_id = 10
        self.site_list[site_id] = Lakeside(site_id, self)
        site_id = 12
        self.site_list[site_id] = Lychee(site_id, self)
        site_id = 14
        self.site_list[site_id] = Supply(site_id, self)
        site_id = 16
        self.site_list[site_id] = BusStation(site_id, self)
        site_id = 18
        self.site_list[site_id] = Stadium(site_id, self)
        site_id = 20
        self.site_list[site_id] = Hospital(site_id, self)
        site_id = 22
        self.site_list[site_id] = Hotel(site_id, self)

    def create_study_room(self, curr_pos):
        self.site_list[curr_pos] = StudyRoom(curr_pos, self)
        self.site_list[curr_pos].sell_site(None, self.game.seatInfo[self.game.curr_player_id].character)
        self.site_list[curr_pos].enter_site(self.game.seatInfo[self.game.curr_player_id])
    
    def create_game_room(self, curr_pos):
        self.site_list[curr_pos] = GameRoom(curr_pos, self)
        self.site_list[curr_pos].sell_site(None, self.game.seatInfo[self.game.curr_player_id].character)
        self.site_list[curr_pos].enter_site(self.game.seatInfo[self.game.curr_player_id])

    def enterRoom(self, EntityCall):
        for i in range(len(self.roomInfo.seats)):
            seat = self.roomInfo.seats[i];
            if seat.userId == 0:
                seat.userId = EntityCall.id;
                seat.entity = EntityCall
                print("玩家进来了---" + str(seat.userId) + " 座位号为 " + str(i))
                EntityCall.changeRoomSeatIndex(i)
                self.base.CanEnterRoom(EntityCall)
                EntityCall.enterRoomSuccess(self.roomKey)
                return

    def enterRoomSeat(self, EntityCall, seatIndex):
        if seatIndex >= len(self.roomInfo.seats):
            return
        seat = self.roomInfo.seats[seatIndex]
        if seat.userId == 0:
            seat.userId = EntityCall.id
            seat.entity = EntityCall
            print("玩家进来了---" + str(seat.userId) + " 座位号为 " + str(seatIndex))
            EntityCall.changeRoomSeatIndex(seatIndex)
            self.base.CanEnterRoom(EntityCall)
            EntityCall.enterRoomSuccess(self.roomKey)
            # self.seated[seatIndex] = 1
        else:
            print('seat already be taken')

    def getSeats(self):
        players = [0,0,0,0]
        for i in range(len(self.roomInfo.seats)):
            seat = self.roomInfo.seats[i]
            if seat.userId != 0:
                players[i] = 1
        INFO_MSG(players)
        return players
        
    def changeRoomSuccess(self, entityID):
        self.roomInfo.clearDataByEntityID(entityID)

    def ReqLeaveRoom(self, EntityCall):
        # 通知玩家base销毁cell
        EntityCall.base.onLeaveRoom()
        # 让base向大厅要人
        self.base.leaveRoom(EntityCall.id)
        # 清除该玩家坐过的椅子数据
        self.roomInfo.clearDataByEntityID(EntityCall.id)

    def reqGetRoomInfo(self, callerEntityID):
        for i in range(len(self.roomInfo.seats)):
            seat = self.roomInfo.seats[i];
            if seat.userId == callerEntityID:
                if (seat.entity.client):
                    seat.entity.client.onGetRoomInfo(self.public_roomInfo)

    def reqChangeReadyState(self, callerEntityID, STATE):
        print(callerEntityID)
        for i in range(len(self.roomInfo.seats)):
            seat = self.roomInfo.seats[i];
            if seat.userId == callerEntityID:
                seat.ready = not STATE
                seat.entity.cell.playerReadyStateChange(seat.ready)
                print(seat.ready)
                break
        for i in range(len(self.roomInfo.seats)):
            seat = self.roomInfo.seats[i];
            if seat.ready == False:
                return
        self.begin()

    # 通过userId获取seatData
    def GetSeatDataByUseId(self, userId):
        for seatData in self.game.gameSeats:
            if seatData.userId == userId:
                return seatData
        return None

    def begin(self):
        self.game = GameController(self.roomInfo, self.playerMaxCount)  # 创建控制器
        self.game.state = "playing"
        self.game.seatInfo[0].entity.cell.start_game()
        self.timer_id = self.one_timer()
        for seat in self.roomInfo.seats:
            self.site_list[0].enter_site(seat)
        self._get_infos()

    def one_timer(self):
        character = self.game.seatInfo[self.game.curr_player_id].character
        if character.is_dead():
            self.game.live_people_num -= 1
            if self.game.is_over():
                self.room_master.cell.end_game()
            else:
                self.game.next_player()
        else:
            if character.rest_day > 0:
                character.rest_one_day()
                self.game.next_player()
                self.one_timer()
            else:
                self.game.seatInfo[self.game.curr_player_id].entity.cell.start_turn()
                
                self.addTimer(100,0,MAIN_TIMER)

    # 由客户端调用？
    def shake(self):
        d1, d2 = self.game.dice.shake()
        seat = self.roomInfo.seats[self.game.curr_player_id]
        # seat.entity.cell.shake_notify(d1,d2)
        self.loop -= 1
        if self.loop == 0:
            for seat in self.roomInfo.seats:
                seat.entity.cell.end_game_rand(random.randint(0,6), seat.seatIndex)
        # seat = self.game.seatInfo[self.game.curr_player_id]
        curr_pos = seat.character.position
        # DEBUG_MSG(self.site_list)
        INFO_MSG("seat_id")
        INFO_MSG(seat.userId)
        INFO_MSG(self.game.curr_player_id)
        if self.site_list[curr_pos] is not None:
            self.site_list[curr_pos].leave_site(self.game.curr_player_id)
        steps = d1 + d2
        if ROOM_MAX_PLAYER == 1:
            steps = 10
        if ROOM_MAX_PLAYER == 2:
            steps = 1
        #if self.game.curr_player_id == 0:
        #    steps = 16
        seat.character.change_position(steps)
        curr_pos = seat.character.position
        seat.entity.cell.move_notify(self.game.curr_player_id, steps)
        site = self.site_list[curr_pos]
        if site == None:
            seat.entity.cell.normal_choose(curr_pos)
            # self.next()
        else:
            site.enter_site(seat)
            site.site_event()

    def next(self):
        self._get_infos()
        self.delTimer(MAIN_TIMER)
        if not self.game.dice.repeat:
            self.game.next_player()
        self.one_timer()

    def _get_infos(self):
        abilitys = [0,0,0,0]
        moneys = [0,0,0,0]
        ranks = [1,2,3,4]
        for i in range(len(self.roomInfo.seats)):
            seat = self.roomInfo.seats[i]
            INFO_MSG(seat.character)
            INFO_MSG(seat.character.money)
            abilitys[i] = seat.character.ability
            moneys[i] = seat.character.money

        for i in range(ROOM_MAX_PLAYER):
            for j in range(i+1,ROOM_MAX_PLAYER):
                if abilitys[j] > abilitys[i]:
                    ranks[j] -= 1
                    ranks[i] += 1
        INFO_MSG(abilitys)
        INFO_MSG(moneys)
        INFO_MSG(ranks)
        self.game.seatInfo[0].entity.cell.update_infos(int(moneys[0]), int(moneys[1]), int(moneys[2]), int(moneys[3]), 
                                                       abilitys[0], abilitys[1], abilitys[2], abilitys[3],
                                                       ranks[0], ranks[1], ranks[2], ranks[3])
    def move_player(self, dest):
        self.site_list[16].move_player(dest)
        if self.site_list[dest] is not None:
            self.site_list[dest].enter_site(self.game.seatInfo[self.game.curr_player_id])

    def immute(self):
        self.site_list[20].escape()

    def stay_hospital(self):
        self.site_list[20].stay_hospital()

    def buy_product(self,im, tra, xiu, boo):
        self.site_list[12].buy_product(im, tra, xiu, boo)

    def teach_select(self, num):
        self.site_list[6].select_event_callback(num)

    def lake_select(self, num):
        self.site_list[10].select_event_callback(num)

    def check_answer(self, num):
        self.site_list[6].check_answer(num)

    def player_study(self, curr_pos):
        self.site_list[curr_pos].player_study()
    
    def player_use_xiuxian_card_study(self, curr_pos):
        self.site_list[curr_pos].player_use_xiuxian_card_study()

    def play_game(self, curr_pos):
        self.site_list[curr_pos].play_game()
    
    def player_use_card(self, curr_pos):
        self.site_list[curr_pos].player_use_card()
# --------------------------------------------------------------------------------------------
#                              Callbacks
# --------------------------------------------------------------------------------------------
    def onTimer(self, tid, userArg):
        """
        KBEngine method.
        引擎回调timer触发
        """
        self.game.seatInfo[self.game.curr_player_id].entity.cell.time_out()
        self.game.next_player()
        self.one_timer()


class GameController:
    def __init__(self, roomInfo, maxPlayerCount):
        self.seatInfo = roomInfo.seats
        self.curr_player_id = 0  # 当前进行游戏的玩家(座位index)
        self.dice = Dice()
        self.state = "waiting"
        self.maxPlayerCount = maxPlayerCount
        self.live_pepole_num = maxPlayerCount

    def next_player(self):
        self.curr_player_id = (self.curr_player_id + 1) % self.maxPlayerCount

    def is_over(self):
        return self.live_pepole_num == 1

# 房间信息
class roomInfo:
    def __init__(self, roomKey, maxPlayerCount):
        self.id = roomKey
        self.seats = []
        for i in range(maxPlayerCount):
            seat = seat_roomInfo(i)
            seat.create_player(self.id)
            self.seats.append(seat)

    def clearData(self):
        for i in range(len(self.seats)):
            self.clearDataBySeat(i, False)

    def clearDataBySeat(self, index, isOut=True):
        s = self.seats[index]
        if isOut:
            s.userId = 0
            s.entity = None
        s.ready = False
        s.score = 0
        s.seatIndex = index

    def clearDataByEntityID(self, entityID, isOut=True):
        for i in range(len(self.seats)):
            if self.seats[i].userId == entityID:
                self.clearDataBySeat(i, isOut)
                break


# 椅子信息
class seat_roomInfo:
    def __init__(self, seatIndex):
        self.userId = 0
        self.entity = None
        self.score = 0
        self.character = None
        self.ready = False
        self.seatIndex = seatIndex

    def create_player(self, room_id):
        self.character = PlayerFactory.create_player(self.seatIndex, room_id, '唐博',self, self.seatIndex)


# 色子
class Dice:
    def __init__(self):
        self.repeat = False  # 如果点数相同继续扔

    def shake(self):
        """
        如果两个筛子点数相同就双倍
        :return:
        """
        self.repeat = False
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.repeat = (dice1 == dice2)
        return dice1, dice2
