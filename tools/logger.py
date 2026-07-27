import logging


def get_logger(name: str):
    """
    Creates and configures a logger instance.

    :param name: Logger name.
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        )
        logger.addHandler(handler)

    return logger
