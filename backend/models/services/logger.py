## To logger.py file
import logging
import logging.handlers

#logging.basicConfig(filename='logs/logs.log', level= logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def get_module_logger(mod_name: str, log_path: str, lvl):
    logger = logging.getLogger(mod_name)
    logger.setLevel(lvl)

    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(funcName)s()-%(message)s')

    file_handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=5000000, backupCount=1)
    #file_handler = logging.Filehandler('logs/logs.log')
    file_handler.setLevel(lvl)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

## To file usage
# from src.logger import get_module_logger
# import logging
# logger = get_module_logger(mod_name=__name__,log_path=f'./logs/{__name__}.log', lvl=logging.INFO)

# logger.info(f'Start getting prediction for {table_name}')
# logger.exception(f'The prediction was obtained for {table_name}')
# logger.info(f'Stop prediction time : {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
