from pydantic import BaseModel

# region Server

class PostServer(BaseModel):
    name: str
    description: str
    client_json_file_id: str
    modded: bool


class PatchServer(BaseModel):
    name: str | None = None
    description: str | None = None
    client_json_file_id: str | None = None
    modded: bool | None = None


class ServerResponse(BaseModel):
    id: int
    name: str
    description: str
    client_json_file_id: str
    modded: bool

    class Config:
        from_attributes = True

# endregion


# region ModPack

class PostModPack(BaseModel):
    server_id: int
    name: str
    description: str
    file_id: str
    required: bool


class PatchModPack(BaseModel):
    server_id: int | None = None
    name: str | None = None
    description: str | None = None
    file_id: str | None = None
    required: bool | None = None


class ModPackResponse(BaseModel):
    id: int
    server_id: int
    name: str
    description: str
    file_id: str
    required: bool

    class Config:
        from_attributes = True

# endregion
