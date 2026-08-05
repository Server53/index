import logging
import pathlib

from .base import IdGenerator

logger = logging.getLogger('files')


class IdGeneratorNumeric(IdGenerator):
    LAST_ID_PATH = pathlib.Path(".last_numeric_id")

    __last_id: int

    def __init__(self, last_id: int):
        self.__last_id = last_id

    @classmethod
    def __get_last_id(cls) -> int:
        last_id_path = IdGeneratorNumeric.LAST_ID_PATH
        try:
            last_id_str = last_id_path.read_text()
            last_id = int(last_id_str)
        except Exception as e:  # noqa
            logger.error(f'Error {e}')
            last_id = 0
        last_id_path.write_text(str(last_id))
        return last_id

    @classmethod
    def __set_last_id(cls, last_id: int):
        last_id_path = IdGeneratorNumeric.LAST_ID_PATH
        last_id_path.write_text(str(last_id))

    @staticmethod
    def setup() -> IdGenerator:
        cls = IdGeneratorNumeric
        last_id = cls.__get_last_id()
        return IdGeneratorNumeric(last_id)

    def generate(self) -> str:
        self.__last_id += 1
        self.__set_last_id(self.__last_id)
        return str(self.__last_id)
