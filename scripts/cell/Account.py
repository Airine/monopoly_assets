from KBEDebug import *


class Account(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)

    def LeaveRoom(self, callerEntityID):
        """
        离开房间
        """
        if callerEntityID != self.id:
            return
        KBEngine.globalData["Room_%i" % self.spaceID].ReqLeaveRoom(self)

    def changeRoomSeatIndex(self, index):
        self.roomSeatIndex = index

    def playerReadyStateChange(self, state):
        self.isReady = state

    def move_notify(self, steps, cur_pos):
        # self.palyer.position += steps;
        if self.client:
            self.client.move(steps, cur_pos)
        self.otherClients.otherPlayerMove(self.id, steps, cur_pos)

    def start_game(self):
        self.allClients.startGame()

    def end_game(self):
        self.allClients.endGame()

    def start_turn(self):
        if self.client:
            self.client.startTurn()
        self.otherClients.otherStartTurn(self.id)

    def normal_choose(self):
        if self.client:
            self.client.normalChoose()
        self.otherClients.otherNormalChoose(self.id)
        pass

    def time_out(self):
        if self.client:
            self.client.timeOut()
        self.otherClients.otherTimeOut(self.id)
    
    def get_rest_in_hospital(self, days, if_immune):
        if self.client:
            if if_immune:
                self.client.useImmunity()
                self.otherClients.otherUseImmunity(self.id)
            else:
                self.client.rest(days)
                self.otherClients.otherPlayerRest(self.id, days)