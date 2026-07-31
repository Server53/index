from abc import ABC, abstractmethod


class IdGenerator(ABC):
    @staticmethod
    @abstractmethod
    def setup() -> "IdGenerator":
        ...

    @abstractmethod
    def generate(self) -> str:
        ...
