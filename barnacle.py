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
        [ 0b11000,
	0b01100,
	0b00110,
	0b00011,
	0b00011,
	0b00110,
	0b01100,
	0b11000 ],
  ]

  lcd.lcd_load_custom_chars(fontdata1)
  lcd.lcd_write(0x80)
  lcd.lcd_write_char(0)
  


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
