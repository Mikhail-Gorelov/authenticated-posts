from fastapi import HTTPException, status
from api.services.security import JwtService
from api.v1.auth.schemas import UserSchema


class LoginService:

    def __init__(self, user: UserSchema):
        self.user = user

    async def authenticate(self):
        if not self.user.username == "user" and self.user.password == "pass":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

    async def generate_response(self) -> dict:
        service = JwtService()
        access_token = service.create_access_token(self.user.username)
        return {
            'access_token': access_token,
        }