import i2c_lcd_driver
import signal
import logging
import knob
import RPi.GPIO as GPIO
import volumio_controller

# The two pins that the encoder uses (BCM numbering).
GPIO_A = 4 
GPIO_B = 17

# The pin that the knob's button is hooked up to.
GPIO_BUTTON = 23

def on_turn(delta):
  if delta == -1:
    volumioCtrl.menuDown()
  else:
    volumioCtrl.menuUp()
  
def on_press(value):
  volumioCtrl.enter()

def setup():
  FORMAT = '%(asctime)-15s %(message)s'
  logging.basicConfig(format=FORMAT,filename='/home/volumio/barnacle/barnacle.log',level=logging.INFO)
  logger = logging.getLogger()
  logger.info('started barnacle')	
	
  GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  global encoder
  encoder  = knob.RotaryEncoder(GPIO_A, GPIO_B, callback=on_turn, buttonPin=GPIO_BUTTON, buttonCallback=on_press)
  global lcd
  lcd = i2c_lcd_driver.lcd()
  lcd.lcd_display_string("barnacle started", 2)
  global volumioCtrl
  volumioCtrl = volumio_controller.VolumioAPI(logger, lcd)
 
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
    #while 1:
      #sleep(0.1)
    #loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
