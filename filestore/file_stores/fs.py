import io
import pathlib
from os import stat_result

from filestore.id_generators.base import IdGenerator

from .base import FileInfo, FileStore


class FileStoreFS(FileStore):
    FILES_PATH = pathlib.Path("uploaded_files")
    CHUNK_SIZE = 32_768  # 32kb

    id_gen: IdGenerator

    def __init__(self, id_gen: IdGenerator):
        self.id_gen = id_gen
        self.FILES_PATH.mkdir(parents=True, exist_ok=True)
    
    def upload(self, file: io.BufferedIOBase) -> str:
        file_id = self.id_gen.generate()
        file_path = self.FILES_PATH.joinpath(file_id)
        file.seek(0)
        with file_path.open('wb') as saved_file:
            while (chunk := file.read(self.CHUNK_SIZE)):
                saved_file.write(chunk)
        return file_id

    def info(self, file_id: str) -> FileInfo:
        file_path = self.FILES_PATH.joinpath(file_id)
        stat_result = file_path.stat()
        file_info = self.__file_info_from_stat(stat_result)
        return file_info

    def download(self, file_id: str) -> io.BufferedIOBase:
        file_path = self.FILES_PATH.joinpath(file_id)
        if not file_path.is_file():
            raise FileNotFoundError(file_path)
        return file_path.open('rb')

    @staticmethod
    def __file_info_from_stat(stat: stat_result) -> FileInfo:
        return FileInfo(
            size=stat.st_size
        )
