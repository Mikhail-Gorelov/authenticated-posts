from datetime import datetime, timedelta
from typing import Any

from fastapi import HTTPException, status

from jose import JWTError, jwt

from core.settings import settings


class JwtService:

    def __init__(
            self,
            access_token_expire_minutes: int = None,
            algorithm: str = None,
    ):
        self.access_token_expire = access_token_expire_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.algorithm = algorithm or settings.ALGORITHM
        self.access_token_secret_key = settings.SECRET_KEY

    def create_access_token(self, subject: str | Any) -> str:
        return self.__get_encoded_jwt(subject, self.access_token_expire, self.access_token_secret_key)

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )

    def __get_encoded_jwt(self, subject: str, expires_minutes: int, secret_key: str) -> str:
        expires_delta = datetime.now() + timedelta(minutes=expires_minutes)
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(
            claims=to_encode,
            key=secret_key,
            algorithm=self.algorithm,
        )
        return encoded_jwt
