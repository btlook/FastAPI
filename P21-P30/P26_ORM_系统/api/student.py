from fastapi import APIRouter

student_api = APIRouter()


@student_api.get("/student")
async def get_all_student():
    return {
        "操作": "查看所有的学生"
    }


@student_api.post("/student")
async def add_student():
    return {
        "操作": "添加一个学生"
    }


@student_api.get("/student/{student_id}")
async def get_one_student(student_id: int):
    return {
        "操作": f"查看id:{student_id}的一个学生"
    }


@student_api.delete("/student/{student_id}")
async def delete_student(student_id: int):
    return {
        "操作": f"删除id={student_id}的学生"
    }


@student_api.put("/student/{student_id}")
async def update_student(student_id: int):
    return {
        "操作": f"更新id={student_id}的学生"
    }
