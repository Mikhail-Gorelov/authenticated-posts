from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from .schemas import PostSchema

from .data import posts_data
from api.services.security import JwtService


async def get_posts():
    return posts_data

async def get_post(post_id: int):
    post = next((post for post in posts_data if getattr(post, "id", None) == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


async def create_post(post: PostSchema, token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    JwtService.verify_token(token)
    post.id = len(posts_data) + 1
    posts_data.append(post)
    return post
