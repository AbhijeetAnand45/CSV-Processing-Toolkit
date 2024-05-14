import logging

def set_log_config(logger):
    print("Handlers ==========> " + str(logger.hasHandlers()))

    fh = logging.FileHandler('PanIndia_ML_Prediction_Loadonbatt.log')
    fh.setLevel(logging.DEBUG)

    # Set the logger's level to log messages of all levels
    logger.setLevel(logging.DEBUG)

    print("Handlers ==========> " + str(logger.hasHandlers()))
    print('logger initialized....\n')
    print('associated handlers - ', len(logger.handlers))

    if len(logger.handlers) > 0:
        return logger
    else:
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)  # Set the console handler to a higher level if you don't want to print INFO messages

        # create formatter and add it to the handlers
        fh_formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(filename)s - Line: %(lineno)d - %(message)s')
        ch_formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(filename)s - Line: %(lineno)d - %(message)s')
        fh.setFormatter(fh_formatter)
        ch.setFormatter(ch_formatter)

        print('logger initialized....\n')
        print('associated handlers - ', len(logger.handlers))
        for handler in logger.handlers:
            print(handler)

        # add the handlers to logger
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger

