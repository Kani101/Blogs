import logging
# from app import logger

class QueryLogger(object):

    def log(self, message):
        # logger.log(level=20, msg=message)
        try:
            logger = logging.getLogger('query')
            logger.debug(message)


        except Exception as e:
            print(e)
