"""
Helpers for setting up sensible logging
"""

import logging
import logging.config
from typing import Any, Dict

import structlog  # type: ignore
from chalice import Chalice  # type: ignore


def configure_logging(app: Chalice):
    """
    Configure structured logging for a Chalice application
    """
    shared_processors = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
    ]

    level = lambda x: "DEBUG" if x.debug else "INFO"

    config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "plain": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(sort_keys=True),
                "foreign_pre_chain": shared_processors,
            }
        },
        "handlers": {
            "default": {"class": "logging.StreamHandler", "formatter": "plain"}
        },
        "loggers": {
            "": {"handlers": ["default"], "level": level(app), "propagate": False}
        },
    }

    config["loggers"][app.app_name] = {
        "handlers": ["default"],
        "level": level(app),
        "propagate": False,
    }

    logging.config.dictConfig(config)
