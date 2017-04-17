from socketIO_client import SocketIO, LoggingNamespace
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT,filename='/home/volumio/barnacle/barnacle.log',level=logging.INFO)
logger = logging.getLogger()
logger.info('volumio api started')

class VolumioAPI:
  
  #global logger
  
  def __init__(self, log):
    self.logger = log
    self.logger.info('volumio socket init: connecting...') 
    self.socketIO = SocketIO('localhost', 3000)
    self.socketIO.on('connect', self.on_connect)
    self.socketIO.on('disconnect', self.on_disconnect)
    self.socketIO.on('reconnect', self.on_reconnect)
    self.socketIO.on('pushState', self.on_pushState)
    self.socketIO.wait(seconds=1)
    self.testLogger()

  def testLogger(self):
    self.logger.info('test logger')
    
  def on_connect(self):
    print('connect')
    self.socketIO.on('pushBrowseSources', self.on_browseSources)
    self.socketIO.emit('getBrowseSources', {})
    self.socketIO.wait(seconds=10)

  def on_browseSources(self, *args):
    print(args)
    
  def on_disconnect(self):
    print('disconnect')

  def on_reconnect(self):
    print('reconnect')
  
  def on_pushState(self, *args):
    print(args)     
    
  def getBrowseableSources(self):
    self.logger.info('get sources')
