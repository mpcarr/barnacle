from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
  print('connect')

def on_disconnect():
  print('disconnect')

def on_reconnect():
  print('reconnect') 

class VolumioAPI:
  
  #global logger
  
  def __init__(self, log):
    self.logger = log
    self.logger.info('volumio socket init: connecting...') 
    socketIO = SocketIO('localhost', 3000)
    socketIO.on('connect', on_connect)
    socketIO.on('disconnect', on_disconnect)
    socketIO.on('reconnect', on_reconnect)
    self.testLogger()

  def testLogger(self):
    self.logger.info('test logger')
    
     
    
  def getBrowseableSources(self):
    self.logger.info('get sources')
