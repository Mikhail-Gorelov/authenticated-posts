from api.v1.auth.schemas import  UserSchema
from api.v1.auth.services import LoginService


async def sign_in_view(data: UserSchema):
    service = LoginService(data)
    await service.authenticate()
    return await service.generate_response()