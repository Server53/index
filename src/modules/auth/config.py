ACCESS_TOKEN_EXPIRE_SECONDS: int = 15 * 60  # 15 minutes
REFRESH_TOKEN_EXPIRE_SECONDS: int = 7 * 60 * 60 * 24  # 7 days
UTC_OFFSET_HOURS: int = 3  # UTC+3 (Moscow time)
JWT_HASH_ALGORITHM: str = 'HS256'
JWT_SECRET_KEY: str = "default-key"