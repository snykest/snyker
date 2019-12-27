"""
Helpers for logging
"""

import logging

import structlog  # type: ignore


def configure_logging(logger, debug: bool = False) -> None:
    """
    Configure structured logging for the specified logger
    """
    shared_processors = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
    ]
    structlog.configure(
        processors=shared_processors
        + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        context_class=structlog.threadlocal.wrap_dict(dict),
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
    )

    renderer = structlog.processors.JSONRenderer(sort_keys=True)

    formatter = structlog.stdlib.ProcessorFormatter(
        processor=renderer, foreign_pre_chain=shared_processors
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.handlers = []
    logger.addHandler(handler)
    if debug:
        logger.setLevel(logging.DEBUG)
