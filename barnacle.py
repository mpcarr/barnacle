import signal
import logging
from socketIO_client import SocketIO, LoggingNamespace

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT,filename='/home/volumio/barnacle/barnacle.log',level=logging.INFO)
logger = logging.getLogger()
logger.info('started barnacle')

print("barnacle")
signal.pause()
