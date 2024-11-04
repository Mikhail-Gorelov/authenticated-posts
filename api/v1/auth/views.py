# app/endpoints.py

# from fastapi import APIRouter, Depends, HTTPException, status
# from app.models import PostSchema, UserLoginSchema
# from app.posts_data import posts
# from app.auth import create_access_token, verify_token
# from fastapi.security import OAuth2PasswordBearer
#
# router = APIRouter()
#
#
#
# @router.post("/token")
# def login(user: UserLoginSchema):
#     # Mock authentication, replace with real user validation
#     if user.username == "user" and user.password == "pass":
#         access_token = create_access_token(data={"sub": user.username})
#         return {"access_token": access_token, "token_type": "bearer"}
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials",
#         )
