from socketIO_client import SocketIO, LoggingNamespace

class VolumioAPI:
  
  global logger
  
  def __init__(self, log):
    logger = log
    logger.info('volumio socket init: connecting...') 
    testLogger()
    socketIO = SocketIO('localhost', 3000)
    socketIO.on('connect', self.on_connect)
    socketIO.on('disconnect', self.on_disconnect)
    socketIO.on('reconnect', self.on_reconnect)

    
  def testLogger()
    logger.info('test logger')
    
  def on_connect(self):
    logger.info('connect')

  def on_disconnect(self):
    logger('disconnect')

  def on_reconnect(self):
    logger('reconnect')    
    
  def getBrowseableSources(self):
    logger.info('get sources')