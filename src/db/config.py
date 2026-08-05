import logging
import sys

logger = logging.getLogger('db')

from src.config import EnvVarNotSet, prefixed_getenv_factory

_ = prefixed_getenv_factory(logger)

try:
    DATABASE_URL = str(_('DATABASE_URL', 'sqlite:///db.sqlite'))
except EnvVarNotSet as e:
    logger.error(f"ERROR: required environment variable not set: {e}")
    sys.exit(1)
