import logging, os
import sys
from pprint import pformat

from fastapi import FastAPI
from loguru import logger
from loguru._defaults import LOGURU_FORMAT
from starlette.requests import Request
from middleware import logger as m_logger

from config import get_settings


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def init(app: FastAPI):
    config = get_settings()
    if not config.log_engine == "loguru":
        return app

    LOGGING_LEVEL = logging.DEBUG if config.DEV else logging.INFO
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")

    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=0)]

    log_file_path = os.path.join(config.log_path, "wise.log")
    err_log_file_path = os.path.join(config.log_path, "wise.err.log")

    loguru_config = {
        "handlers": [
            {
                "sink": sys.stderr,
                "level": "DEBUG",
                "format": "<green>{time:YYYY-mm-dd HH:mm:ss.SSS}</green> |"
                + " {thread.name} |"
                + " <level>{level}</level> |"
                + " <cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> -"
                " <level>{message}</level>",
            },
            {"sink": log_file_path, "rotation": "00:00", "encoding": "utf-8"},
            {
                "sink": err_log_file_path,
                "serialize": True,
                "level": "ERROR",
                "rotation": "00:00",
                "encoding": "utf-8",
            },
        ]
    }

    logger.configure(**loguru_config)
    m_logger.init(app)
    return app
