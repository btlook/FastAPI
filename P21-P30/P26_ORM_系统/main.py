from fastapi import FastAPI
import uvicorn

from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM

app = FastAPI()

# fastapi 一旦运行, register_tortoise 就开始执行,实现监控
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,# 如果数据库为空,则自动生成对应表单,生产环境不要开
    # add_exception_handlers=True,# 生产环境不要开,会泄露调试信息
)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)
