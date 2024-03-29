from socketIO_client import SocketIO, LoggingNamespace
from time import sleep
import Queue
import threading
import json
from pprint import pprint

QUEUE = Queue.Queue()
EVENT = threading.Event()

class VolumioApi:

  def __init__(self, log, lcd):
    self.logger = log
    self.lcd = lcd
    self.logger.info('volumio socket init: connecting...')
    self.connected = False
    self.lcd.lcd_clear()
    self.lcd.lcd_display_string("Volumio connecting..", 2)

    self.currentState = 0;
    self.states = {0: self.browseSources
               }

    self.menuLines = 0

    menuArrow = [
      [0b11000,
       0b01100,
       0b00110,
       0b00011,
       0b00011,
       0b00110,
       0b01100,
       0b11000],
      [0b00000,
       0b00000,
       0b00000,
       0b00000,
       0b00000,
       0b00000,
       0b00000,
       0b00000]
    ]

    self.lcd.lcd_load_custom_chars(menuArrow)
      
    self.lines = [0x80, 0xC0, 0x94, 0xd4]
    
    def connect_to_socket(q, port):
      try:
        #sleep(10); # Give volumio time to come up
        self.logger.info("connecting to socket on thread")
        self.socket = SocketIO('localhost', port)
        self.socket.on('connect', self.on_connect)
        self.socket.on('disconnect', self.on_disconnect)
        self.socket.on('reconnect', self.on_reconnect)
        self.socket.wait(seconds=1)
        q.put(1)
      except:
        self.logger.info("caught ex")
         
    q = Queue.Queue()
    t = threading.Thread(target=connect_to_socket, args = (q, 3000))
    t.daemon = True
    t.start()
    
    connection_timeout = 60
    while connection_timeout > 0 and self.connected is False:
      try:
        one = q.get(False) 
        if self.connected == True:
          connection_timeout = 0
      except Queue.Empty:
        if self.connected == True:
          connection_timeout = 0
        else:
          self.lcd.lcd_clear()
          self.lcd.lcd_display_string("Volumio connecting..", 2)
          self.lcd.lcd_display_string("Timeout in  {}".format(connection_timeout), 3)
          sleep(1)
          connection_timeout = connection_timeout - 1
      
    if self.connected == True:  
      self.socket.on('pushBrowseSources', self.on_browseSources)
      self.lcd.lcd_clear()
      self.lcd.lcd_display_string("CONNECTED", 2)
      self.socket.emit('getBrowseSources')
      self.socket.wait(seconds=1)
    else:
      self.lcd.lcd_clear()
      self.lcd.lcd_display_string("FAILED TO CONNECT", 2)

    self.lcd.lcd_write(0x02)  # return home
    self.lcd.lcd_write(0x80)  # line 1 pos 1
    self.currentLine = 0
    self.lcd.lcd_write(self.lines[self.currentLine])
    self.lcd.lcd_write_char(0)

      
  def menuDown(self):
    QUEUE.put(-1)
    
  def menuUp(self):
    QUEUE.put(1)
    
  def enter(self):
    QUEUE.put(2)
    
  def on_connect(self):
    self.connected = True
    #self.lcd.lcd_clear()    
    #self.lcd.lcd_display_string("CONNECTED", 2)
    #self.socketIO.emit('getBrowseSources', {})
    #self.socketIO.wait(seconds=1)

  def on_browseSources(self, *args):
    #self.logger.info(args[0])
    data = json.dumps(args[0])
    data = json.loads(data)
    self.logger.info(data)
    line = 1
    self.lcd.lcd_clear()
    self.menuLines = len(data)
    for musicSource in data:
      self.logger.info(musicSource["name"])	
      if line < 5:	
        self.lcd.lcd_display_string(musicSource["name"],line,1)
        line = line + 1
    
  def on_disconnect(self):
    print('disconnect')

  def on_reconnect(self):
    print('reconnect')

  def process_lcd(self):
    while not QUEUE.empty():
      cmd = QUEUE.get()
      self.states[self.currentState](cmd)

  def browseSources(self, cmd):
    #menu navigation or select
    if cmd == -1:
      #menu down
      self.currentLine = self.currentLine + 1
      # clear the selection arrow
      self.lcd.lcd_write(0x02)  # return home
      self.lcd.lcd_write(0x80)  # line 1 pos 1

      if self.currentLine == 0:
        self.lcd.lcd_write(self.lines[3])
        self.lcd.lcd_write_char(1)
      else:
        self.lcd.lcd_write(self.lines[self.currentLine-1])
        self.lcd.lcd_write_char(1)

      self.lcd.lcd_write(self.lines[self.currentLine])
      self.lcd.lcd_write_char(0)
      # self.logger.info('menu down')

      if self.currentLine == 4:
        self.currentLine = 0
        # sleep(0.1)
    else:
      if cmd == 1:
        # clear the selection arrow
        self.lcd.lcd_write(0x02)  # return home
        self.lcd.lcd_write(0x80)  # line 1 pos 1
        # self.lcd.lcd_display_string("A")

        if self.currentLine == 0:
          self.lcd.lcd_write(self.lines[3])
          self.lcd.lcd_write_char(1)
        else:
          self.lcd.lcd_write(self.lines[self.currentLine-1])
          self.lcd.lcd_write_char(1)

        self.lcd.lcd_write(self.lines[self.currentLine])
        self.lcd.lcd_write_char(0)
        # self.logger.info('menu down')
        self.currentLine = self.currentLine - 1
        if self.currentLine == 4:
          self.currentLine = 0
          # sleep(0.1)
        #menu up
      else:
        print("selected")