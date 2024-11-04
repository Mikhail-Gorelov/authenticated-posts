from api.services.base_router import BaseRouter
from api.v1.posts import views
from api.v1.posts.schemas import PostSchema


class PostsRouter(BaseRouter):

    def __init__(self):
        super().__init__()
        self._router.add_api_route(
            path='/posts',
            endpoint=views.get_posts,
            response_model=list[PostSchema],
            methods=['GET'],
        )
        self._router.add_api_route(
            path='/posts/{post_id}',
            endpoint=views.get_post,
            response_model=PostSchema,
            methods=['GET'],
        )
        self._router.add_api_route(
            path='/posts',
            endpoint=views.create_post,
            methods=['POST'],
        )