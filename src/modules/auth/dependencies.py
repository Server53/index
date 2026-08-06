from fastapi import HTTPException, Request

from . import logic


def authorized_admin(request: Request) -> str:
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        raise HTTPException(401, detail='Unauthorized')
    BEARER_PREFIX = 'Bearer '
    if not auth_header.startswith(BEARER_PREFIX):
        raise HTTPException(401, detail='Unauthorized')
    access_token = auth_header[len(BEARER_PREFIX):]
    try:
        payload = logic.validate_access_token(access_token)
        return payload.name
    except logic.InvalidToken:
        raise HTTPException(401, detail='Unauthorized')
    