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

# The pin that the knob's button is hooked up to. If you have no button, set
# this to None.
GPIO_BUTTON = 23

# This callback runs in the background thread. All it does is put turn
# events into a queue and flag the main thread to process them. The
# queueing ensures that we won't miss anything if the knob is turned
# extremely quickly.
def on_turn(delta):
  print("%f", delta);
  #QUEUE.put(delta)
  #EVENT.set()
  
def on_press(value):
  print("Toggled button")
  #EVENT.set()  

def setup():
  GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
  encoder = knob.RotaryEncoder(GPIO_A, GPIO_B, callback=on_turn, buttonPin=GPIO_BUTTON, buttonCallback=on_press)

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
