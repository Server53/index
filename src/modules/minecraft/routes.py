from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.db.session import get_session

from .models import MinecraftModPack, MinecraftServer
from .request_models import ModPackResponse, PostModPack, PostServer

router = APIRouter()


@router.get("/servers")
def get_servers():
    with get_session() as session:
        servers = session.query(MinecraftServer).all()
    server_models = [ModPackResponse.model_validate(s) for s in servers]
    return {"servers": server_models}


@router.get("/modpacks/{server_id}")
def get_modpacks(server_id: int):
    with get_session() as session:
        modpacks = session.query(MinecraftModPack).filter_by(server_id=server_id).all()
    modpack_models = [ModPackResponse.model_validate(m) for m in modpacks]
    return {"modpacks": modpack_models}


@router.post("/server")
def post_server(payload: PostServer):
    with get_session() as session:
        new_server = MinecraftServer(**payload.model_dump())
        session.add(new_server)
        session.commit()
        session.refresh(new_server)
    server_response = ModPackResponse.model_validate(new_server)
    return JSONResponse(server_response.model_dump(), status_code=201)


@router.post("/modpack")
def post_modpack(payload: PostModPack):
    with get_session() as session:
        new_modpack = MinecraftModPack(**payload.model_dump())
        session.add(new_modpack)
        session.commit()
        session.refresh(new_modpack)
    modpack_response = ModPackResponse.model_validate(new_modpack)
    return JSONResponse(modpack_response.model_dump(), status_code=201)


@router.delete("/server/{server_id}")
def delete_server(server_id: int):
    with get_session() as session:
        deleted = session.query(MinecraftServer).filter_by(server_id=server_id).delete()
        session.commit()
    return JSONResponse({"deleted": deleted})
