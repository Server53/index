from abc import ABC, abstractmethod


class Hasher(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> bytes:
        """ Returns encrypted version of `text` """
        ...

    @abstractmethod
    def check(self, text: str, hash: bytes) -> bool:
        """ Returns True if `text` corresponds to `hash` """
        ...
