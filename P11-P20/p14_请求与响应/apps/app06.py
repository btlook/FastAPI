from fastapi import APIRouter
from fastapi import Request

app06 = APIRouter()


@app06.post("/items")
async def items(request: Request):
    print("URL:", request.url)
    print("客户端IP地址: ", request.client.host)
    print("客户端宿主: ", request.headers.get("user-agent"))
    print("cookies: ", request.cookies)

    return {
        "URL": request.url,
        "IP": request.client.host,
        "Cookies": request.cookies,
        "User-Agent": request.headers.get("user-agent"),
    }
