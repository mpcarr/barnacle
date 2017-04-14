import signal
import logging
from socketIO_client import SocketIO, LoggingNamespace

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT,filename='barnacle.log')
logger = logging.getLogger()
logger.info('started barnacle')

print("barnacle")
signal.pause()
