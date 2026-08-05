import logging
import os

ENV_PREFIX = "S53I_"

class EnvVarNotSet(Exception): ...

def prefixed_getenv_factory(logger: logging.Logger):
    def prefixed_getenv(name: str, default = None):
        prefixed_name = ENV_PREFIX+name
        value = os.getenv(prefixed_name, default)
        if value is None:
            raise EnvVarNotSet(prefixed_name)
        logger.info(f'{prefixed_name}: {value}')
        return value
    return prefixed_getenv
