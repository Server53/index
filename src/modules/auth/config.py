import logging
import sys

from src.config import EnvVarNotSet, prefixed_getenv_factory

logger = logging.getLogger('auth')

_ = prefixed_getenv_factory(logger)

try:
    ACCESS_TOKEN_EXPIRE_SECONDS = int(_('ACCESS_TOKEN_EXPIRE_SECONDS', 15*60))  # 15 minutes
    REFRESH_TOKEN_EXPIRE_SECONDS = int(_('REFRESH_TOKEN_EXPIRE_SECONDS', 7*60*60*24))  # 7 days
    UTC_OFFSET_HOURS = int(_('UTC_OFFSET_HOURS', 3))  # UTC+3 (Moscow time)
    JWT_HASH_ALGORITHM = str(_('JWT_HASH_ALGORITHM', 'HS256'))
    JWT_SECRET_KEY = str(_('JWT_SECRET_KEY', 'default-key'))
except EnvVarNotSet as e:
    logger.error(f"ERROR: required environment variable not set: {e}")
    sys.exit(1)
