import bcrypt

from .base import Hasher


class BCryptHasher(Hasher):
    def encrypt(self, text: str) -> bytes:
        bytes = text.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        return hash

    def check(self, text: str, hash: bytes) -> bool:
        text_bytes = text.encode('utf-8')
        return bcrypt.checkpw(text_bytes, hash)
