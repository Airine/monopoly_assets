import random
from player.CsPlayer import CsPlayer
from player.PlayerFactory import PlayerFactory
from KBEDebug import *

MAIN_TIMER = 1

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
        self.site_list = list()
        self.seated = [0,0,0,0]

    def pass_site(self, site_list):
       self.site_list = site_list

    # TODO: 重写enterRoom
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
            self.site_list[0].cell.enter_site(seat)

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
        # seat = self.game.seatInfo[self.game.curr_player_id]
        seat = self.roomInfo.seats[self.game.curr_player_id]
        curr_pos = seat.character.position
        # DEBUG_MSG(self.site_list)
        INFO_MSG("seat_id")
        INFO_MSG(seat.userId)
        INFO_MSG(self.game.curr_player_id)
        self.site_list[curr_pos].cell.leave_site(self.game.curr_player_id)
        steps = d1 + d2  
        if self.game.curr_player_id == 0:
            steps = 20
        seat.character.change_position(steps)
        curr_pos = seat.character.position
        seat.entity.cell.move_notify(self.game.curr_player_id, steps)
        site = self.site_list[curr_pos]
        if site == None:
            seat.entity.cell.normal_choose()
            # self.next()
        else:
            site.cell.enter_site(seat)
            site.cell.site_event()
        self.next()

    def next(self):
        self.delTimer(MAIN_TIMER)
        if not self.game.dice.repeat:
            self.game.next_player()
        self.one_timer()


# --------------------------------------------------------------------------------------------
#                              Callbacks
# --------------------------------------------------------------------------------------------
def onTimer(self, tid, userArg):
    """
    KBEngine method.
    引擎回调timer触发
    """
    self.game.entity.cell.time_out()
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
        self.character = PlayerFactory.create_player(self.seatIndex, room_id, '唐博',self, 1)


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
