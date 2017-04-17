from socketIO_client import SocketIO, LoggingNamespace

class VolumioAPI:
  
  def __init__(self, logger):
    self.logger = logger
    self.logger.info('started barnacle') 
    socketIO = SocketIO('localhost', 3000)
    socketIO.on('connect', on_connect)
    socketIO.on('disconnect', on_disconnect)
    socketIO.on('reconnect', on_reconnect)
    
  def on_connect(self):
    self.logger.info('connect')

  def on_disconnect(self):
    self.logger('disconnect')

  def on_reconnect(self):
    self.logger('reconnect')    
    
  def getBrowseableSources(self):
    self.logger.info('get sources')
