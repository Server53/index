from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.db.session import get_session
from src.modules.auth.dependencies import authorized_admin

from .db.models import MinecraftModPack, MinecraftServer
from .models import (
    ModPackResponse,
    PatchModPack,
    PatchServer,
    PostModPack,
    PostServer,
    ServerResponse,
)

router = APIRouter()


# region Server

@router.get("/servers")
def get_servers():
    with get_session() as session:
        servers = session.query(MinecraftServer).all()
    server_models = [ServerResponse.model_validate(s) for s in servers]
    return {"servers": server_models}


@router.post("/server", response_model=ServerResponse)
def post_server(payload: PostServer, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        new_server = MinecraftServer(**payload.model_dump())
        session.add(new_server)
        session.commit()
        session.refresh(new_server)
    server_response = ServerResponse.model_validate(new_server)
    return JSONResponse(server_response.model_dump(), status_code=201)


@router.patch("/server/{server_id}", response_model=ServerResponse)
def patch_server(server_id: int, payload: PatchServer, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        server = session.get(MinecraftServer, server_id)
        if not server:
            raise HTTPException(404, detail="Server not found")
        for (key, value) in payload.model_dump().items():
            if value is not None:
                setattr(server, key, value)
        session.commit()
    server_response = ServerResponse.model_validate(server)
    return JSONResponse(server_response.model_dump(), status_code=214)


@router.put("/server/{server_id}", response_model=ServerResponse)
def put_server(server_id: int, payload: PostServer, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        server = session.get(MinecraftServer, server_id)
        if not server:
            raise HTTPException(404, detail="Server not found")
        for (key, value) in payload.model_dump().items():
            if value is not None:
                setattr(server, key, value)
        session.commit()
    server_response = ServerResponse.model_validate(server)
    return JSONResponse(server_response.model_dump(), status_code=214)


@router.delete("/server/{server_id}")
def delete_server(server_id: int, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        deleted = session.query(MinecraftServer).filter_by(id=server_id).delete()
        session.commit()
    return JSONResponse({"deleted": deleted})

# endregion


# region ModPack

@router.get("/modpacks/{server_id}")
def get_modpacks(server_id: int):
    with get_session() as session:
        modpacks = session.query(MinecraftModPack).filter_by(server_id=server_id).all()
    modpack_models = [ModPackResponse.model_validate(m) for m in modpacks]
    return {"modpacks": modpack_models}


@router.post("/modpack")
def post_modpack(payload: PostModPack, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        new_modpack = MinecraftModPack(**payload.model_dump())
        session.add(new_modpack)
        session.commit()
        session.refresh(new_modpack)
    modpack_response = ModPackResponse.model_validate(new_modpack)
    return JSONResponse(modpack_response.model_dump(), status_code=201)


@router.patch("/modpack/{modpack_id}", response_model=ModPackResponse)
def patch_modpack(modpack_id: int, payload: PatchModPack, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        modpack = session.get(MinecraftModPack, modpack_id)
        if not modpack:
            raise HTTPException(404, detail="ModPack not found")
        for (key, value) in payload.model_dump().items():
            if value is not None:
                setattr(modpack, key, value)
        session.commit()
    modpack_response = ModPackResponse.model_validate(modpack)
    return JSONResponse(modpack_response.model_dump(), status_code=214)


@router.put("/modpack/{modpack_id}", response_model=ModPackResponse)
def put_modpack(modpack_id: int, payload: PostModPack, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        modpack = session.get(MinecraftModPack, modpack_id)
        if not modpack:
            raise HTTPException(404, detail="ModPack not found")
        for (key, value) in payload.model_dump().items():
            if value is not None:
                setattr(modpack, key, value)
        session.commit()
    modpack_response = ServerResponse.model_validate(modpack)
    return JSONResponse(modpack_response.model_dump(), status_code=214)


@router.delete("/modpack/{modpack_id}")
def delete_modpack(modpack_id: int, username: Annotated[str, Depends(authorized_admin)]):
    with get_session() as session:
        deleted = session.query(MinecraftModPack).filter_by(id=modpack_id).delete()
        session.commit()
    return JSONResponse({"deleted": deleted})

# endregion
