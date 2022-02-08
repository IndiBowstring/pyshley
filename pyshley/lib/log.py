import logging
from datetime import datetime

currDate = datetime.now().strftime('%Y-%m-%d')

logger = logging.getLogger('pyshley')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename=('log/' + currDate + '.log'), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)