from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base


class MinecraftServer(Base):
    __tablename__ = "minecraft_server"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, name="server_id")
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)
    client_json_file_id: Mapped[str] = mapped_column(String(256))
    modded: Mapped[bool] = mapped_column()

    modpacks: Mapped[list["MinecraftModPack"]] = relationship(back_populates="server")


class MinecraftModPack(Base):
    __tablename__ = "minecraft_modpack"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, name="modpack_id")
    server_id: Mapped[int] = mapped_column(ForeignKey("minecraft_server.server_id"))
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)
    required: Mapped[bool] = mapped_column()
    file_id: Mapped[str] = mapped_column(String(256))

    server: Mapped["MinecraftServer"] = relationship(back_populates="modpacks")