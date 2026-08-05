import logging

logger = logging.getLogger('files')
logger.info('Initializing files...')

from . import config  # noqa
from .routes import router

__all__ = [
    "router"
]
