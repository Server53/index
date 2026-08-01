from .base import Hasher
from .bcrypt import BCryptHasher

hasher: Hasher = BCryptHasher()


__all__ = [
    "Hasher",
    "hasher"
]