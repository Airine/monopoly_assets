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

    # def shake_notify(self, dice_1, dice_2):
    #    pass

    def move_notify(self, seat_index, steps):
        # self.palyer.position += steps;
        if self.client:
            self.allClients.move(seat_index, steps)

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
        self.otherClients.otherNormalChoose()
        pass

    def time_out(self):
        if self.client:
            self.client.timeOut()
        self.otherClients.otherTimeOut(self.id)
    
    def close_events(self):
        if self.client:
            self.allClients.closeEvents()
       
    def update_infos(self, m1, a1, r1, m2, a2, r2, m3, a3, r3, m4, a4, r4):
        if self.client:
            self.allClients.updateInfo(m1, a1, r1, m2, a2, r2, m3, a3, r3, m4, a4, r4)
    
    #AdminBuilding
    def show_send_money(self, money):
        if self.client:
            self.client.sendMoney(money)
        self.otherClients.otherSendMoney(money)

    #Building one

    def exam(self):
        if self.client:
            self.client.exam()
            self.otherClients.otherExam()

    def quiz(self, num):
        if self.client:
            self.client.quiz(num)
            self.otherClients.otherQuiz(num)

    def show_cheat_warning(self):
        if self.client:
            self.client.showCheatWarning()

    def show_get_study_ability(self,ab_num):
        if self.client:
            self.client.showGetStudyAbility(ab_num)

    #BusStation
    def select_position_to_move(self):
        if self.client:
            self.client.selectPositionToMove()

    #Canteen

    def random_event(self,num):
        if self.client:
            self.client.randomEvent(num)
            self.otherClients.otherRandomEvent(num)

    #GameRoom
    def show_enter_game(self,game_pay,level, type):
        if self.client:
            self.client.showEnterGame(game_pay,level, type)

    def show_weather_to_buy(self,owner,price):
        if self.client:
            self.client.showWeatherToBuy(owner,price)

    def show_building_update(self,location):
        if self.client:
            self.client.showBuildingUpdate(location)

    def show_building_downgrade(self,location):
        if self.client:
            self.client.showBuildingDowngrade(location)

    # Hospital
    def get_rest_in_hospital(self, days, if_immune):
        if self.client:
            self.client.rest(days, if_immune)
            self.otherClients.otherPlayerRest(days, if_immune)

    # 选择事件
    def select_event(self, site_id, id):
        if self.client:
            self.client.selectEvent(site_id, id)
            self.otherClients.otherSelectEvent(site_id, id)

    def run_successful(self):
        if self.client:
            self.client.runSuccessful()

    def run_fail(self):
        if self.client:
            self.client.runFail()

    # Lychee

    def show_shop(self,money):
        if self.client:
            self.client.showShop(money)
            self.otherClients.otherShowShop(money)

    # Stadium

    # StudyRoom
    def show_enter_study(self,a, b, c_bool,level):
        if self.client:
            self.client.showEnterStudy(a, b, c_bool,level)

    # Supply
    def select_building(self):
        if self.client:
            self.client.selectBuilding()

    def select_building_again(self):
        if self.client:
            self.client.selectBuildingAgain()

    def show_destory_building(self,location):
        if self.client:
            self.client.showDestoryBuilding(location)

    def on_create_study_room(self, curr_pos):
        if self.client:
            self.allClients.onCreateStudyRoom(curr_pos)

    def on_create_game_room(self, curr_pos):
        if self.client:
            self.allClients.onCreateGameRoom(curr_pos)