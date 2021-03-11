import logging


def logger():
    logging.basicConfig(filename='app.log', filemode='a',
                        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p')
    return logging


log = logger()
