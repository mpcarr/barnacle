import i2c_lcd_driver
import signal
import logging
import knob
import RPi.GPIO as GPIO
from socketIO_client import SocketIO, LoggingNamespace

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT,filename='/home/volumio/barnacle/barnacle.log',level=logging.INFO)
logger = logging.getLogger()
logger.info('started barnacle')

# The two pins that the encoder uses (BCM numbering).
GPIO_A = 4 
GPIO_B = 17

# The pin that the knob's button is hooked up to.
GPIO_BUTTON = 23

def on_turn(delta):
  if delta == -1:
    print("clockwise")
  else:
    print("anti-clockwise")
  
def on_press(value):
  print("button pressed")

def setup():
  GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  global encoder
  encoder  = knob.RotaryEncoder(GPIO_A, GPIO_B, callback=on_turn, buttonPin=GPIO_BUTTON, buttonCallback=on_press)
  global lcd
  lcd = i2c_lcd_driver.lcd()
  lcd.lcd_display_string("barnacle", 2)
  fontdata1 = [
        # char(0) - Upper-left character
        [ 0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b11111, 
          0b11111 ],

        # char(1) - Upper-middle character
        [ 0b00000, 
          0b00000, 
          0b00100, 
          0b00110, 
          0b00111, 
          0b00111, 
          0b11111, 
          0b11111 ],
        
        # char(2) - Upper-right character
        [ 0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b10000, 
          0b11000 ],
        
        # char(3) - Lower-left character
        [ 0b11111, 
          0b11111, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000 ],
       
        # char(4) - Lower-middle character
        [ 0b11111, 
          0b11111, 
          0b00111, 
          0b00111, 
          0b00110, 
          0b00100, 
          0b00000, 
          0b00000 ],
        
        # char(5) - Lower-right character
        [ 0b11000, 
          0b10000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000 ],
      ]

  lcd.lcd_load_custom_chars(fontdata1)

  lcd.lcd_write(0x80 + 84)
  lcd.lcd_write_char(0)
  lcd.lcd_write_char(1)
  lcd.lcd_write_char(2)

  #lcd.lcd_write(0xC0)
  #lcd.lcd_write_char(3)
  #lcd.lcd_write_char(4)
  #lcd.lcd_write_char(5)

  #lcd.lcd_load_custom_chars(fontdata1)
  #lcd.lcd_write(0x80)
  #lcd.lcd_write_char(0)
  


#def loop():
	#global globalCounter
	#while True:
		#rotaryDeal()
    #print 'globalCounter = %d' % globalCounter

def destroy():
  encoder.destroy()

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    print("barnacle")
    signal.pause()
    #loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
