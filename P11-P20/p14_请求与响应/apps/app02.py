from fastapi import APIRouter
from typing import Union, Optional

# Optional[str] = Union[str, None]

app02 = APIRouter()


@app02.get("/jobs/{kd}")
async def get_jobs(kd, xl: Union[str, None], gj: Optional[str]=None):  # 有默认参数即认为参数为可选项
    # 基于kd,xl,gj,数据库查询岗位信息
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }
