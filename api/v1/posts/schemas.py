from pydantic import BaseModel
from typing import Optional


class PostSchema(BaseModel):
    id: Optional[int] = None
    title: str
    text: str
