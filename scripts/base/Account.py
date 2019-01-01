# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import Functor

MAIN_STATE_IDEL = 1
MAIN_STATE_MATCH = 2
MAIN_STATE_INGAME = 3

class Account(KBEngine.Proxy):
    def __init__(self):
        KBEngine.Proxy.__init__(self)
        self.MainState = MAIN_STATE_IDEL
        self.roomKey = 0;

    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        DEBUG_MSG(id, userArg)

    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
        cell部分。
        """
        INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))

    def onLogOnAttempt(self, ip, port, password):
        """
        KBEngine method.
        客户端登陆失败时会回调到这里
        """
        INFO_MSG(ip, port, password)
        return KBEngine.LOG_ON_ACCEPT

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        DEBUG_MSG("Account[%i].onClientDeath:" % self.id)

    # self.destroy()

    def reqCreateAvatar(self, name):
        # 客户端请求创建一个角色
        # 0：表示请求成功
        # 1：已经有相同名字的玩家
        # 2：创建失败！已经有一个角色了
        if self.isNewPlayer == 0:
            self.client.OnReqCreateAvatar(2)
            return

        porps = {
            "playerName": name,
        }
        nameEntity = KBEngine.createEntityLocally("CheckName", porps)
        if nameEntity:
            nameEntity.writeToDB(Functor.Functor(self._OnNameSave, name))

    def _OnNameSave(self, name, success, avatar):
        if self.isDestroyed:
            if avatar:
                avatar.destroy()
            return
        if success:
            self.isNewPlayer = 0
            self.playerName_base = name;
            self.playerID_base = self.databaseID + 10000
            self.playerName = name
            self.playerID = self.playerID_base
            # self.cellData["playerName"] = name
            # self.cellData["playerID"] = self.playerID_base
            if self.client:
                self.client.OnReqCreateAvatar(0)
        else:
            self.client.OnReqCreateAvatar(1)

    def onLeaveRoom(self):
        self.destroyCellEntity()

    def createCell(self, roomCell):
        self.createCellEntity(roomCell)

    def onLoseCell(self):
        self.MainState = MAIN_STATE_IDEL
        if self.client:
            self.client.playerLevelRoom()

    def enterRoomSuccess(self, roomKey):
        self.roomKey = roomKey

    def reqChangeRoom(self):
        KBEngine.globalData["Halls"].changeRoom(self, self.roomKey)

    # 房间通知玩家换房间
    def OnTeleport(self, space):
        print("开始换房间，当前房间号---" + str(self.roomKey))
        self.teleport(space)

    # 换房间成功回调
    def onTeleportSuccess(self):
        print("换房间成功，当前房间号---" + str(self.roomKey))

    def changeRoomSeatIndex(self, index):
        if self.cell:
            self.cell.changeRoomSeatIndex(index);
        else:
            self.cellData["roomSeatIndex"] = index

    def EnterMatchesMatch(self):
        if self.MainState != MAIN_STATE_IDEL:
            return
        self.MainState = MAIN_STATE_MATCH
        KBEngine.globalData["Halls"].EnterMatchesMatch(self)

    def CreatePrivateRoom(self):
        if self.MainState != MAIN_STATE_IDEL:
            return
        self.MainState = MAIN_STATE_INGAME
        KBEngine.globalData["Halls"].CreatePrivateRoom(self)

    def EnterPrivateRoom(self, room_id):
        #if self.MainState != MAIN_STATE_IDEL:
        #    return
        #self.MainState = MAIN_STATE_INGAME
        #KBEngine.globalData["Halls"].joinRoom(self, int(room_id))
        if KBEngine.globalData["Halls"].getRoom(int(room_id)):
            self.roomKey = int(room_id)

    def Next(self):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.next()
        self.cell.close_events()

    def ShakeDice(self):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.shake()

    def EnterRoomSeat(self, seat_id):
        KBEngine.globalData["Halls"].joinRoomSeat(self, int(self.roomKey), int(seat_id))
        # KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).enterRoomSeat(self, int(seat_id))

    def RequestRoomSeat(self):
        seated = [0,0,0,0]    
        INFO_MSG("avaliable seats")
        INFO_MSG(seated)
        if self.client:
            self.client.InitialChoosePanel(seated[0], seated[1], seated[2], seated[3])

    # Create Study or Game room
    def createStudyRoom(self, curr_pos):
        room = KBEngine.globalData["Halls"].getRoom(int(self.roomKey))
        room.cell.create_study_room(curr_pos)
        self.cell.on_create_study_room(curr_pos)

    def createGameRoom(self, curr_pos):
        room = KBEngine.globalData["Halls"].getRoom(int(self.roomKey))
        room.cell.create_game_room(curr_pos)
        self.cell.on_create_game_room(curr_pos)
    
    # Hosipital
    def Immute(self):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.immute()

    def StayHospital(self):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.stay_hospital()

    # Lychee
    def BuyGoods(self, im, tra, xiu, boo):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.buy_product(im, tra, xiu, boo)

    # Bus Station
    def MoveTo(self, dest):
        # KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).site_list[16].move_player(dest)
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.move_player(dest)

    # Teaching
    def Teach(self, num):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.teach_select(num)

    def Lake(self, num):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.lake_select(num)

    # Building One
    def Quiz(self, num):
        KBEngine.globalData["Halls"].getRoom(int(self.roomKey)).cell.check_answer(num)
