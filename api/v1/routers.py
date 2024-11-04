from fastapi import APIRouter
from .auth.routers import AuthRouter
from .posts.routers import PostsRouter

router = APIRouter()
common_prefix = '/api/v1'

router.include_router(AuthRouter().router, prefix=common_prefix)
router.include_router(PostsRouter().router, prefix=common_prefix)