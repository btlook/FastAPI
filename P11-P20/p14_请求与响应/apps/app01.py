from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/user/1")
async def get_user():
    print(id)
    return {
        "user_id": "root user"
    }

@app01.get("/user/{id}")
async def get_user(id):
    print(id)
    return {
        "user_id": id
    }


@app01.get("/article/{id}")
async def get_article(id: int):
    print(id)
    return {
        "article": id
    }
