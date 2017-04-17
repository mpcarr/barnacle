from socketIO_client import SocketIO, LoggingNamespace
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT,filename='/home/volumio/barnacle/barnacle.log',level=logging.INFO)
logger = logging.getLogger()
logger.info('volumio api started')

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
    socketIO.wait(seconds=1)
    self.testLogger()

  def testLogger(self):
    self.logger.info('test logger')
    
     
    
  def getBrowseableSources(self):
    self.logger.info('get sources')
