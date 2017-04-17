from socketIO_client import SocketIO, LoggingNamespace

class VolumioAPI:
  
  #global logger
  
  def __init__(self, log):
    self.logger = log
    self.logger.info('volumio socket init: connecting...') 
    socketIO = SocketIO('localhost', 3000)
    socketIO.on('connect', self.on_connect)
    socketIO.on('disconnect', self.on_disconnect)
    socketIO.on('reconnect', self.on_reconnect)
    self.testLogger()

  def testLogger(self):
    self.logger.info('test logger')
    
  def on_connect(self):
    self.logger.info('connect')

  def on_disconnect(self):
    self.logger('disconnect')

  def on_reconnect(self):
    self.logger('reconnect')    
    
  def getBrowseableSources(self):
    self.logger.info('get sources')
