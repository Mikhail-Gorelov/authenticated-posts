from fastapi import APIRouter
from .auth.routers import AuthRouter
from .posts.routers import PostsRouter

router = APIRouter()

router.include_router(AuthRouter().router, prefix='/api/v1')
router.include_router(PostsRouter().router, prefix='/api/v1')