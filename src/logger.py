import logging


def get_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    """

    logger = logging.getLogger(
        "async_file_processor"
    )

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        (
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


logger = get_logger()