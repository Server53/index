from pydantic import BaseModel


class PostServer(BaseModel):
    name: str
    description: str
    client_json_file_id: str
    modded: bool


class PostModPack(BaseModel):
    server_id: int
    name: str
    description: str
    required: bool
    file_id: str


class ModPackResponse(BaseModel):
    id: int
    name: str
    description: str
    client_json_file_id: int
    modded: bool

    class Config:
        from_attributes = True


class ModPackResponse(BaseModel):
    id: int
    server_id: int
    name: str
    description: str
    file_id: int
    required: bool

    class Config:
        from_attributes = True