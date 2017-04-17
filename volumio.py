from socketIO_client import SocketIO, LoggingNamespace
from time import sleep

class VolumioAPI:
  
  #global logger
  
  def __init__(self, log, lcd):
    self.logger = log
    self.lcd = lcd
    self.logger.info('volumio socket init: connecting...')
    self.lcd.lcd_clear()
    self.lcd.lcd_display_string("Volumio connecting..", 2)
    self.socketIO = SocketIO('localhost', 3000)
    self.socketIO.on('connect', self.on_connect)
    self.socketIO.on('disconnect', self.on_disconnect)
    self.socketIO.on('reconnect', self.on_reconnect)
    self.socketIO.on('pushBrowseSources', self.on_browseSources)
    
    connection_timeout = 60
    while connection_timeout > 0 or self.connected:
      self.lcd.lcd_clear()
      self.lcd.lcd_display_string("Volumio connecting..", 2)
      self.lcd.lcd_display_string("Timeout in  {}".format(connection_timeout), 3)
      self.socketIO.wait(seconds=1)
      sleep(1)
      connection_timeout = connection_timeout - 1
   
  def menuDown():
    self.logger.info('menu down')
    
  def menuUp():
    self.logger.info('menu up')
    
  def enter():
    self.logger.info('enter')
    
  def on_connect(self):
    self.connected = true
    #self.lcd.lcd_clear()    
    #self.lcd.lcd_display_string("CONNECTED", 2)
    #self.socketIO.emit('getBrowseSources', {})
    #self.socketIO.wait(seconds=1)

  def on_browseSources(self, *args):
    self.logger.info(args)
    
  def on_disconnect(self):
    print('disconnect')

  def on_reconnect(self):
    print('reconnect')
