import KBEngine
import Functor
from KBEDebug import *

class Canteen(KBEngine.Entity):
	
	def __init__(self):
		KBEngine.Entity.__init__(self)
		self.createCellEntityInNewSpace(None)
		self.name = self.cellData["name"]
		self.site_id = self.cellData["room"]
		self.location = self.cellData["location"]
		self.curr_player = self.cellData["curr_player"]

