from fastapi import APIRouter, HTTPException, Request

from . import logic
from .models import LoginModel

router = APIRouter()


@router.post("/login")
def admin_login(payload: LoginModel):
    try:
        logic.login(payload.name, payload.password)
        pair = logic.generate_tokens(payload.name)
        logic.store_refresh_token(pair.refresh)
        return logic.get_tokens_response(pair)
    except logic.InvalidPassword:
        raise HTTPException(401, detail="Invalid password")
    except logic.UserNotFound:
        raise HTTPException(401, detail="User not found")


@router.post("/refresh")
def admin_refresh(request: Request):
    try:
        refresh_token = logic.extract_refresh_token(request)
        payload = logic.validate_refresh_token(refresh_token)
        pair = logic.generate_tokens(payload.name)
        logic.store_refresh_token(pair.refresh)
        logic.revoke_refresh_token(refresh_token)
        return logic.get_tokens_response(pair)
    except logic.NoRefreshToken:
        raise HTTPException(401, detail="No refresh_token cookie")
    except logic.InvalidToken:
        raise HTTPException(401, detail="Invalid refresh_token")
    except logic.ExpiredToken:
        raise HTTPException(401, detail="Expired refresh_token")
    except logic.RevokedToken:
        raise HTTPException(401, detail="Revoked refresh_token")
