LOG_ON_ACCEPT=1    
LOG_ON_REJECT =1    
LOG_ON_WAIT_FOR_DESTROY =1    
LOG_TYPE_DBG =1    
LOG_TYPE_ERR =1    
LOG_TYPE_INFO =1    
LOG_TYPE_NORMAL =1    
LOG_TYPE_WAR =1    
NEXT_ONLY =1    
component = ""
entities = {}
baseAppData = {} 
globalData={} 

#cell属性  
cellAppData ={}   
component=""


def addWatcher( path, dataType, getFunction ):
	"base cell 都有 成员函数" 
	pass
def address( ):
	"base cell 都有 成员函数" 
	pass 
def MemoryStream( ):
	"base cell 都有 成员函数" 
	pass 
def charge( ordersID, dbID, byteDatas, pycallback ):
	"base成员函数" 
	pass 
def createEntity( ):
	"base成员函数" 
	pass 
def createEntityAnywhere( entityType, *params, callback ):
	"base成员函数" 
	pass 
def createEntityRemotely( entityType, baseMB, *params, callback ):
	"base成员函数"  
	pass
def createEntityFromDBID( entityType, dbID, callback, dbInterfaceName ):
	"base成员函数"  
	pass
def createEntityAnywhereFromDBID( entityType, dbID, callback, dbInterfaceName ):
	"base成员函数" 
	pass 
def createEntityRemotelyFromDBID( entityType, dbID, baseMB, callback, dbInterfaceName ): 
	"base成员函数"
	pass 
def createEntityLocally( entityType, *params ): 
	"base成员函数"
	pass 
def debugTracing( ): 
	"base cell 都有 成员函数" 
	pass 
def delWatcher( path ): 
	"base cell 都有 成员函数" 
	pass 
def deleteEntityByDBID( entityType, dbID, callback, dbInterfaceName ): 
	"base成员函数"
	pass
def deregisterReadFileDescriptor( fileDescriptor ):  
	"base cell 都有 成员函数" 
	pass
def deregisterWriteFileDescriptor( fileDescriptor ):
	"base cell 都有 成员函数" 
	pass  
def executeRawDatabaseCommand( command, callback, threadID, dbInterfaceName ): 
	"base cell 都有 成员函数" 
	pass 
def genUUID64( ): 
	"base cell 都有 成员函数" 
	pass 
def getResFullPath( res ): 
	"base cell 都有 成员函数" 
	pass
def getWatcher( path ): 
	"base cell 都有 成员函数" 
	pass
def getWatcherDir( path ): 
	"base cell 都有 成员函数" 
	pass
def getAppFlags( ):  
	"base cell 都有 成员函数" 
	pass
def hasRes( res ):
	"base cell 都有 成员函数" 
	pass
def isShuttingDown( ): 
	"base cell 都有 成员函数" 
	pass 
def listPathRes( path, extension ): 
	"base cell 都有 成员函数" 
	pass
def lookUpEntityByDBID( entityType, dbID, callback, dbInterfaceName ): 
	"base成员函数" 
	pass
def matchPath( res ):
	"base cell 都有 成员函数" 
	pass 
def open( res, mode ): 
	"base cell 都有 成员函数" 
	pass
def publish( ):
	"base cell 都有 成员函数"   
	pass 
def quantumPassedPercent( ): 
	"base成员函数"
	pass 
def registerReadFileDescriptor( fileDescriptor, callback ): 
	"base cell 都有 成员函数" 
	pass
def registerWriteFileDescriptor( fileDescriptor, callback ): 
	"base cell 都有 成员函数" 
	pass
def reloadScript( fullReload ): 
	"base cell 都有 成员函数" 
	pass 
def scriptLogType( logType ): 
	"base cell 都有 成员函数" 
	pass 
def setAppFlags( flags ):  
	"base cell 都有 成员函数" 
	pass
def time( ): 
	"base cell 都有 成员函数" 
	pass
def onBaseAppReady( isBootstrap ):
	"base回调函数"
	pass  
def onBaseAppShutDown( state ):
	"base回调函数"
	pass  
def onCellAppDeath( addr ):
	"base回调函数"
	pass  
def onFini( ):
	"base回调函数"
	pass  
def onBaseAppData( key, value ): 
	"base回调函数"
	pass 
def onBaseAppDataDel( key ):
	"base回调函数"
	pass  
def onGlobalData( key, value ):
	"base cell 都有 回调函数"
	pass 
def onGlobalDataDel( key ): 
	"base cell 都有 回调函数"
	pass 
def onInit( isReload ):
	"base cell 都有 回调函数"
	pass  
def onLoseChargeCB( orderID, dbID, success, datas ):
	"base回调函数" 
	pass 
def onReadyForLogin( isBootstrap ): 
	"base回调函数"
	pass 
def onReadyForShutDown( ):
	"base回调函数" 
	pass 
def onAutoLoadEntityCreate( entityType, dbID ):
	"base回调函数"
	pass  
#--------------------cell KBEngine成员函数----------------------
def addSpaceGeometryMapping( spaceID, mapper, path, shouldLoadOnServer, params ):
	"cell成员函数"
	pass     
def createEntity( entityType, spaceID, position, direction, params ):
	"cell成员函数"
	pass    
def delSpaceData( spaceID, key ):
	"cell成员函数"
	pass   
def getSpaceData( spaceID, key ):
	"cell成员函数" 
	pass 
def getSpaceGeometryMapping( spaceID ):
	"cell成员函数" 
	pass         
def raycast( spaceID, layer, src, dst ):
	"cell成员函数" 
	pass   
def setSpaceData( spaceID, key, value ):
	"cell成员函数"
	pass  
def onCellAppData( key, value ):
	"cell回调函数"
	pass  
def onCellAppDataDel( key ):
	"cell回调函数"
	pass    
def onSpaceData( spaceID, key, value ):
	"cell回调函数"
	pass  
def onSpaceGeometryLoaded( spaceID, mapping ):
	"cell回调函数"
	pass  
def onAllSpaceGeometryLoaded( spaceID, isBootstrap, mapping ):
	"cell回调函数"
	pass  


class Entity:
	cell=1 
	cellData={}
	className=""
	client=1
	databaseID=1 
	databaseInterfaceName=""
	id = 1 
	isDestroyed=False  
	shouldAutoArchive  = True
	shouldAutoBackup  = True 

	#cell 属性
	allClients="" 
	base=""
	client=""
	controlledBy=""
	className=""
	direction = float  
	hasWitness =False 
	isWitnessed =False
	layer  =1  
	otherClients = "" 
	position =float  
	spaceID =1 
	topSpeed =  float  
	topSpeedY =  float  
	volatileInfo =  float  

	def addTimer( self, initialOffset, repeatOffset=0, userArg=0 ):  
		"base cell 都有 成员函数" 
		pass
	def createCellEntity( self, cellEntityMB ): 
		"base成员函数"  
		pass
	def createCellEntityInNewSpace( self, cellappIndex ):
		"base成员函数" 
		pass  
	def delTimer( self, id ): 
		"base cell 都有 成员函数"   
		pass
	def destroy( self, deleteFromDB, writeToDB ): 
		"base成员函数" 
		pass 
	def destroyCellEntity( self ): 
		"base成员函数"  
		pass
	def teleport( self, baseEntityMB ):
		"base成员函数"   
		pass
	def writeToDB( self, callback, shouldAutoLoad, dbInterfaceName ):  
		"base成员函数" 
		pass
	def onCreateCellFailure( self ):
		"base回调函数"  
		pass
	def onDestroy( self ):
		"base cell 都有 回调函数"  
		pass
	def onGetCell( self ):
		"base回调函数" 
		pass 
	def onLoseCell( self ):
		"base回调函数" 
		pass 
	def onPreArchive( self ):
		"base回调函数"
		pass  
	def onRestore( self ): 
		"base cell 都有 回调函数" 
		pass
	def onTimer( self, timerHandle, userData ): 
		"base cell 都有 回调函数"
		pass 
	def onTeleportFailure( self ):
		"base cell 都有 回调函数" 
		pass
	def onTeleportSuccess( self, nearbyEntity ):
		"base回调函数"  
		pass
	def onWriteToDB( self, cellData ): 
		"base回调函数"
		pass 

	def accelerate( self, accelerateType, acceleration ):
		"cell成员函数"
		pass  
	def addYawRotator( self, targetYaw, velocity, userArg ):
		"cell成员函数"
		pass  
	def addProximity( self, range, userArg ):
		"cell成员函数"
		pass   
	def cancelController( self, controllerID ):
		"cell成员函数"
		pass  
	def clientEntity( self, destID ):
		"cell成员函数"
		pass  
	def canNavigate( self ):
		"cell成员函数"
		pass  
	def debugView( self ):
		"cell成员函数"
		pass   
	def destroy( self ):
		"cell成员函数"
		pass  
	def destroySpace( self ):
		"cell成员函数"
		pass  
	def entitiesInView( self ):
		"cell成员函数"
		pass  
	def entitiesInRange( self, range, entityType=None, position=None ):
		"cell成员函数"
		pass  
	def isReal( self ):
		"cell成员函数"
		pass  
	def moveToEntity( self, destEntityID, velocity, distance, userData, faceMovement, moveVertically ):
		"cell成员函数"
		pass  
	def moveToPoint( self, destination, velocity, distance, userData, faceMovement, moveVertically ):
		"cell成员函数"
		pass  
	def getViewRadius( self ):
		"cell成员函数"
		pass  
	def getViewHystArea( self ):
		"cell成员函数"
		pass  
	def getRandomPoints( self, centerPos, maxRadius, maxPoints, layer ):
		"cell成员函数"
		pass  
	def navigate( self, destination, velocity, distance, maxMoveDistance, maxSearchDistance, faceMovement, layer, userData ):
		"cell成员函数"
		pass  
	def navigatePathPoints( self, destination, maxSearchDistance, layer ):
		"cell成员函数"
		pass  
	def setViewRadius( self, radius, hyst=5 ):
		"cell成员函数"
		pass  
	def teleport( self, nearbyMBRef, position, direction ):
		"cell成员函数"
		pass  
	def writeToDB( self, shouldAutoLoad, dbInterfaceName ):
		"cell成员函数"
		pass  
	def onEnterTrap( self, entity, rangeXZ, rangeY, controllerID, userArg ):
		"cell回调函数"
		pass  
	def onEnteredView( self, entity ):
		"cell回调函数"
		pass  
	def onGetWitness( self ):
		"cell回调函数"
		pass  
	def onLeaveTrap( self, entity, rangeXZ, rangeY, controllerID, userArg ):
		"cell回调函数"
		pass  
	def onLoseControlledBy( self, id ):
		"cell回调函数"
		pass  
	def onLoseWitness( self ):
		"cell回调函数"
		pass  
	def onMove( self, controllerID, userData ):
		"cell回调函数"
		pass  
	def onMoveOver( self, controllerID, userData ):
		"cell回调函数"
		pass  
	def onMoveFailure( self, controllerID, userData ):
		"cell回调函数"
		pass    
	def onSpaceGone( self ):
		"cell回调函数"
		pass  
	def onTurn( self, controllerID, userData ):
		"cell回调函数"
		pass  
	def onTeleport( self ):
		"cell回调函数"
		pass   
	def onTeleportSuccess( self, nearbyEntity ):
		"cell回调函数"
		pass  
	def onUpdateBegin( self ):
		"cell回调函数"
		pass  
	def onUpdateEnd( self ):
		"cell回调函数"
		pass  
	def onWitnessed( self, isWitnessed ):
		"cell回调函数"
		pass  
	def onWriteToDB( self ):
		"cell回调函数"
		pass  


class Proxy(Entity):
	__ACCOUNT_NAME__ =""
	__ACCOUNT_PASSWORD__ =""
	clientAddr=""
	clientEnabled=False
	hasClient=False
	roundTripTime=""
	timeSinceHeardFromClient=""

	def disconnect( self ):
		"base成员函数"   
		pass
	def getClientType( self ): 
		"base成员函数" 
		pass 
	def getClientDatas( self ):
		"base成员函数" 
		pass  
	def giveClientTo( self, proxy ): 
		"base成员函数"  
		pass
	def streamFileToClient( self, resourceName, desc="", id=-1 ): 
		"base成员函数" 
		pass
	def streamStringToClient( self, data, desc="", id=-1 ): 
		"base成员函数"  
		pass
	def onClientDeath( self ):
		"base回调函数" 
		pass
		
	def onClientGetCell( self ):
		"base回调函数"
		pass  
	def onClientEnabled( self ): 
		"base回调函数"
		pass 
	def onGiveClientToFailure( self ):
		"base回调函数" 
		pass 
	def onLogOnAttempt( self, ip, port, password ):
		"base回调函数" 
		pass 
	def onStreamComplete( self, id, success ):
		"base回调函数"
		pass  


	

	
