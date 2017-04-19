from socketIO_client import SocketIO, LoggingNamespace
from time import sleep
import Queue
import threading

class VolumioApi:
  
  #global logger
  def connect_to_socket(q):
    socket = SocketIO('localhost', 3000)
    socket.on('connect', self.on_connect)
    socket.on('disconnect', self.on_disconnect)
    socket.on('reconnect', self.on_reconnect)
    socket.wait(seconds=1)
    q.put(socket)
  
  def __init__(self, log, lcd):
    self.logger = log
    self.lcd = lcd
    self.logger.info('volumio socket init: connecting...')
    self.connected = False
    self.lcd.lcd_clear()
    self.lcd.lcd_display_string("Volumio connecting..", 2)
    
    
    q = Queue.Queue()
    t = threading.Thread(target=self.connect_to_socket, args = (q))
    t.daemon = True
    t.start()
    
    self.socketIO = q.get()
    self.socketIO.on('pushBrowseSources', self.on_browseSources)
    self.lcd.lcd_display_string("After Socket..", 3)
    
    connection_timeout = 60
    while connection_timeout > 0 and self.connected == False:
      if self.connected:
        connection_timeout = 0
      else:
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string("Volumio connecting..", 2)
        self.lcd.lcd_display_string("Timeout in  {}".format(connection_timeout), 3)
        self.socketIO.wait(seconds=1)
        #sleep(1)
        connection_timeout = connection_timeout - 1
      
    self.lcd.lcd_clear()
    self.lcd.lcd_display_string("CONNECTED", 2)
   
  def menuDown(self):
    self.logger.info('menu down')
    
  def menuUp(self):
    self.logger.info('menu up')
    
  def enter(self):
    self.logger.info('enter')
    
  def on_connect(self):
    self.connected = True
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
