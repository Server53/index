import io
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class FileInfo:
    size: int


class FileStore(ABC):
    @abstractmethod
    def upload(self, file: io.BufferedIOBase) -> str:
        ...

    @abstractmethod
    def info(self, file_id: str) -> FileInfo:
        ...

    @abstractmethod
    def download(self, file_id: str) -> io.BufferedIOBase:
        ...

    @abstractmethod
    def delete(self, file_id: str) -> bool:
        ...
