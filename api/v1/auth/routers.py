from api.services.base_router import BaseRouter
from api.v1.auth import views


class AuthRouter(BaseRouter):

    def __init__(self):
        super().__init__()
        self._router.add_api_route(
            path='/sign-in',
            endpoint=views.sign_in_view,
            methods=['POST'],
        )