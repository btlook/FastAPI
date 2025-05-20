from fastapi import APIRouter

user = APIRouter()


@user.post("/login")
def user_login():
    return {"user": "login"}


@user.post("/reg")
def shop_food():
    return {"user": "reg"}
