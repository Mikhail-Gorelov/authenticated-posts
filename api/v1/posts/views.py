from fastapi import  HTTPException
from .schemas import PostSchema

from .data import posts


async def get_posts():
    return posts

async def get_post(post_id: int):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


async def create_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post)
    return post
