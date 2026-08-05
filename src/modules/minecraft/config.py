import logging
import sys

from src.config import EnvVarNotSet, prefixed_getenv_factory

logger = logging.getLogger('minecraft')

_ = prefixed_getenv_factory(logger)

try:
    # Your environment variables here:
    # VAR_NAME = str(_('VAR_NAME', default=''))
    ...
except EnvVarNotSet as e:
    logger.error(f"ERROR: required environment variable not set: {e}")
    sys.exit(1)
