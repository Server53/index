from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Admin(Base):
    __tablename__ = "admin"

    name: Mapped[str] = mapped_column(String(128), primary_key=True)
    password_hash: Mapped[str] = mapped_column(String(256))


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    value: Mapped[str] = mapped_column(String(256), primary_key=True)
    revoked: Mapped[bool] = mapped_column(default=False)
