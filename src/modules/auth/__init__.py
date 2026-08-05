import logging

logger = logging.getLogger('auth')
logger.info('Initializing auth...')

from . import config  # noqa
from .routes import router

__all__ = [
    "router"
]
