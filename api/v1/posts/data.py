from typing import List

from api.v1.posts.schemas import PostSchema

posts = [
    {"id": 1, "title": "Penguins", "text": "Penguins are a group of aquatic flightless birds."},
    {"id": 2, "title": "Tigers", "text": "Tigers are the largest living cat species and a member of the genus Panthera."},
    {"id": 3, "title": "Koalas", "text": "Koala is an arboreal herbivorous marsupial native to Australia."},
]

posts_data: List[PostSchema] = [PostSchema(**post) for post in posts]