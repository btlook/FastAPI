from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def home():
    return {"user_id": 10806}


@app.get("/shop")
async def shop():
    return {"shop": "商品信息"}


if __name__ == '__main__':
    uvicorn.run("p10_quickstart:app", port=8090, reload=True,log_level="debug")
