from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/items",tags=["这是items测试接口","我增加一个tag"],
          summary="this is item测试 summary",
          description="详情....",
          response_description="响应详情",
          deprecated=False)

async def test():
    return {"items": "items数据"}

if __name__ == '__main__':
    uvicorn.run("p11_路径参数:app", port=8020, reload=True)