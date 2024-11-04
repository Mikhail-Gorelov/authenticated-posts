from fastapi.testclient import TestClient
from core.settings import settings
from main import app
from jose import jwt
import pytest


client = TestClient(app)

test_user = {
    "username": "user",
    "password": "pass"
}

def create_test_token():
    token = jwt.encode({"subject": test_user["username"]}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token


@pytest.fixture(scope="module")
def test_user_token():
    return create_test_token()

def test_login_success():
    response = client.post("/api/v1/sign-in", json=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_posts():
    response = client.get("/api/v1/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post_success(test_user_token):
    response = client.post(
        "/api/v1/posts",
        headers={"Authorization": f"Bearer {test_user_token}"},
        json={"title": "New Post", "text": "This is a new post."}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New Post"

def test_create_post_unauthorized():
    response = client.post("/api/v1/posts", json={"title": "New Post", "text": "This is a new post."})
    assert response.status_code == 401

def test_get_specific_post():
    post_id = 1
    response = client.get(f"/api/v1/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_get_specific_post_not_found():
    post_id = 9999
    response = client.get(f"/api/v1/posts/{post_id}")
    assert response.status_code == 404

def test_create_post_invalid_data(test_user_token):
    response = client.post(
        "/api/v1/posts",
        headers={"Authorization": f"Bearer {test_user_token}"},
        json={"title": ""}
    )
    assert response.status_code == 422