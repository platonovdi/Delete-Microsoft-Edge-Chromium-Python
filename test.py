# import logging

# logger = logging.getLogger('logger')
# logger.setLevel(logging.INFO)
# logging.debug('дебаг')
# logging.error('ошибка')
# logging.info('info')

import sys
import logging
from logging import StreamHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='logs.log', filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
handler = StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

logger.debug('debug information')
