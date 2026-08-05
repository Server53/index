import logging

logger = logging.getLogger('minecraft')

logger.info('Initializing minecraft...')

from . import config  # noqa
from .routes import router

__all__ = [
    "router"
]
