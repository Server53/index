import datetime
from collections import namedtuple
from dataclasses import dataclass
from typing import Literal

from . import config
from .time_utils import datetime_from_timestamp_with_tz, datetime_now_with_tz


@dataclass
class JWTPayload:
    name: str
    type: Literal["access", "refresh"]
    issued_at: datetime.datetime
    expires_at: datetime.datetime

    def expired(self) -> bool:
        time_now = datetime_now_with_tz()
        return self.expires_at <= time_now

    def to_dict(self) -> dict:
        return {
            "sub": self.name,
            "type": self.type,
            "iat": int(self.issued_at.timestamp()),
            "exp": int(self.expires_at.timestamp()),
        }

    @staticmethod
    def from_dict(payload: dict) -> "JWTPayload":
        try:
            return JWTPayload(
                name=payload["sub"],
                type=payload["type"],
                issued_at=datetime_from_timestamp_with_tz(payload["iat"]),
                expires_at=datetime_from_timestamp_with_tz(payload["exp"]),
            )
        except KeyError as e:
            raise ValueError(e)

    @staticmethod
    def for_access_token(name: str) -> "JWTPayload":
        time_now = datetime_now_with_tz()
        timeout_seconds = config.ACCESS_TOKEN_EXPIRE_SECONDS
        timeout = datetime.timedelta(seconds=timeout_seconds)
        return JWTPayload(
            name=name, type="access", issued_at=time_now, expires_at=time_now + timeout
        )

    @staticmethod
    def for_refresh_token(name: str) -> "JWTPayload":
        time_now = datetime_now_with_tz()
        timeout_seconds = config.REFRESH_TOKEN_EXPIRE_SECONDS
        timeout = datetime.timedelta(seconds=timeout_seconds)
        return JWTPayload(
            name=name, type="refresh", issued_at=time_now, expires_at=time_now + timeout
        )


TokenPair = namedtuple('TokenPair', ['access', 'refresh'])
