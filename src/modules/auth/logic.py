import jwt
from fastapi import Request, Response
from fastapi.responses import JSONResponse

from src.db.session import get_session

from . import config
from .db.models import Admin, RefreshToken
from .hashing import hasher
from .tokens import JWTPayload, TokenPair


class UserNotFound(Exception): ...


class InvalidPassword(Exception): ...


class NoRefreshToken(Exception): ...


class InvalidToken(Exception): ...


class ExpiredToken(Exception): ...


class RevokedToken(Exception): ...


def login(name: str, password: str):
    with get_session() as session:
        admin = session.query(Admin).filter_by(name=name).first()
        if admin is None:
            raise UserNotFound(name)
        password_ok = hasher.check(password, admin.password_hash.encode())
        if not password_ok:
            raise InvalidPassword(password)


def generate_tokens(name: str) -> TokenPair:
    access_token = jwt.encode(
        payload=JWTPayload.for_access_token(name).to_dict(),
        key=config.JWT_SECRET_KEY,
        algorithm=config.JWT_HASH_ALGORITHM,
    )
    refresh_token = jwt.encode(
        payload=JWTPayload.for_refresh_token(name).to_dict(),
        key=config.JWT_SECRET_KEY,
        algorithm=config.JWT_HASH_ALGORITHM,
    )
    return TokenPair(access=access_token, refresh=refresh_token)


def store_refresh_token(refresh_token: str):
    with get_session() as session:
        db_token = RefreshToken(value=refresh_token)
        session.add(db_token)
        session.commit()


def get_tokens_response(pair: TokenPair) -> Response:
    response = JSONResponse({"access_token": pair.access})
    response.set_cookie(
        key="refresh_token",
        value=pair.refresh,
        httponly=True,
        samesite="lax",
        secure=True,
    )
    return response


def extract_refresh_token(request: Request) -> str:
    try:
        return request.cookies["refresh_token"]
    except KeyError:
        raise NoRefreshToken


def decode_token(refresh_token: str) -> JWTPayload:
    try:
        payload = jwt.decode(
            jwt=refresh_token,
            key=config.JWT_SECRET_KEY,
            algorithms=[config.JWT_HASH_ALGORITHM],
        )
        return JWTPayload.from_dict(payload)
    except jwt.InvalidTokenError:
        raise InvalidToken


def validate_access_token(access_token: str) -> JWTPayload:
    payload = decode_token(access_token)
    if payload.expired():
        raise ExpiredToken
    return payload


def validate_refresh_token(refresh_token: str) -> JWTPayload:
    payload = decode_token(refresh_token)
    if payload.expired():
        raise ExpiredToken
    with get_session() as session:
        db_token = session.query(RefreshToken).filter_by(value=refresh_token).first()
        if db_token is None:
            raise InvalidToken
        if db_token.revoked:
            raise RevokedToken
    return payload


def revoke_refresh_token(refresh_token: str):
    with get_session() as session:
        (
            session.query(RefreshToken)
            .filter_by(value=refresh_token)
            .update({"revoked": True})
        )
        session.commit()
