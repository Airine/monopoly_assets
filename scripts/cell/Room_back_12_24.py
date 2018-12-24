import random
from player.CsPlayer import CsPlayer
from KBEDebug import *

TIMER_HAS_NO_OP_CB = 1


class Room(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        KBEngine.addSpaceGeometryMapping(self.spaceID, None, "spaces/mjRoom")
        KBEngine.globalData["Room_%i" % self.spaceID] = self
        print("Change scene")
        self.roomInfo = roomInfo(self.roomKey, self.playerMaxCount)
        self.room_master = self.EnterPlayerList[0]
        self.game = None

    # self.clearPublicRoomInfo()

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
        self.room_master.cell.start_game()
        self.timer_id = self.one_timer()

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
                self.addTimer(30)

    # 由客户端调用？
    def shake(self):
        d1, d2 = self.game.dice.shake()
        seat = self.game.seatInfo[self.game.curr_player_id]
        curr_pos = seat.character.position
        self.base.site_list[curr_pos].leave_site(seat.entity)
        steps = d1 + d2  # seat.character.change_position(steps)
        seat.entity.move_notify(steps)
        curr_pos = seat.character.position
        site = self.base.site_list[curr_pos]
        # if site == None:
        if True:
            seat.entity.cell.normal_choose()
        else:
            site.enter_site(seat)
            site.site_event()
        self.next()

    def next(self):
        self.delTime(1)
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
        self.seatInfo = roomInfo.seats.sort()
        self.curr_player_id = 0  # 当前进行游戏的玩家(座位index)
        self.dice = Dice()
        self.state = "waiting"
        self.maxPlayerCount = maxPlayerCount
        self.live_pepole_num = maxPlayerCount

    def next_player(self):
        self.player_now = (self.player_now + 1) % self.maxPlayerCount

    def is_over(self):
        return self.live_pepole_num == 1


# 椅子信息
class Seat:
    def __init__(self, seatIndex, room_id, name="test", user_id=0, major="CS"):
        self.userId = user_id
        self.entity = None
        self.character = CsPlayer(self.userId, room_id, name, self, major)
        self.ready = False
        self.seatIndex = seatIndex
        self.taken = False
        self.priority = 0

    def __lt__(self, other):
        return self.priority < other.priority


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


# 房间信息
class roomInfo:
    def __init__(self, roomKey, maxPlayerCount):
        self.id = roomKey
        self.seats = []
        for i in range(maxPlayerCount):
            seat = Seat(i, roomKey)
            self.seats.append(seat)
        self.rank = []
        self.update_rank()

    def update_rank(self):
        pass

    def clearData(self):
        for i in range(len(self.seats)):
            self.clearDataBySeat(i, False)

    def clearDataBySeat(self, index, isOut=True):
        s = self.seats[index]
        if isOut:
            s.userId = 0
            s.entity = None
        s.ready = False
        s.seatIndex = index
        s.priority = 0

    def clearDataByEntityID(self, entityID, isOut=True):
        for i in range(len(self.seats)):
            if self.seats[i].userId == entityID:
                self.clearDataBySeat(i, isOut)
                break
