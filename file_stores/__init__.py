from ..id_generators import id_generator
from .base import FileInfo, FileStore
from .fs import FileStoreFS

file_store: FileStore = FileStoreFS(id_generator)

__all__ = [
    "FileInfo",
    "FileStore",
    "file_store"
]