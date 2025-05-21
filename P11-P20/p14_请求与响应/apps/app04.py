from datetime import datetime, date

from fastapi import APIRouter
from fastapi import Form

app04 = APIRouter()



# Form 表单就表示了'Content-Type: application/x-www-form-urlencoded' \
@app04.post("/regin")
async def regin(username: str = Form(...), password: str = Form(...)):
    print(f"username: {username},password: {password}")
    # 既然是注册,就是数据库的添加操作
    return {
        "username": username,
    }
