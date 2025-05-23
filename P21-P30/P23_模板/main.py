from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index")
async def index(request: Request):
    name = "root"
    age = 15

    books = ["金瓶梅", "聊斋", "剪灯新话", "国色天香"]
    booksDict = {
        "金瓶梅": {"price": 100, "publish": "苹果出版社"},
        "聊斋": {"price": 200, "publish": "橘子出版社"}
    }

    user_dict = {"name": "rain", "age": 20, "gender": "male"}
    pai = 3.1415926

    movies = {
        "Adult":["日韩","欧美","香港"],
        "Unadult":["黑猫警长","熊大熊二","大头儿子"]
    }


    return templates.TemplateResponse(
        "index.html",  # 模板文件
        {
            "request": request,
            "user": name,
            "age": age,
            "books": books,
            "booksDict": booksDict,
            "user_dict": user_dict,
            "pai": pai,
            "movies": movies,
        },  # context 上下文对象,一个字典
    )


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)

