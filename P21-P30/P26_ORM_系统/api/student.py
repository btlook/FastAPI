from typing import List

from fastapi import APIRouter

from models import *
from fastapi import Request
from fastapi.templating import Jinja2Templates

student_api = APIRouter()


@student_api.get("/")
async def get_all_student():
    # (1) 查询所有 all 方法
    # students = await Student.all() # Queryset [Student(),Student()..]
    # print("students",students)
    # for stu in students:
    #     print(stu.name, stu.sno)

    # (2) 过滤查询 filter
    # student = await Student.filter(name="rain")
    # print(student)

    # (3) get 方法
    # student = await Student.get(name="steven")
    # return student

    # (4) 模糊查询
    # student = await Student.filter(sno__gt=2002)
    # print(student)

    # student = await Student.filter(sno__in=[2001,2003])
    # student = await Student.filter(sno__range=[2000,10000])

    # (5) values 查询
    student = await  Student.filter(sno__lt=2003).values("name", "pwd")
    print(student)

    return student


@student_api.get("/index")
async def getAllStudent(request: Request):
    templates = Jinja2Templates(directory="templates")
    students = await Student.all()
    # print(students)
    # for student in students:
    #     print(student.name)
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "students": students,
        }
    )


from pydantic import BaseModel, validator, field_validator


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @field_validator("name")
    def check_name(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

    @field_validator("sno")
    def sno_validat(cls, value):
        assert 2000 < value < 10000, '学号必须在2000到10000之间'
        return value


#
@student_api.post("/")
async def add_student(Student_In: StudentIn):
    # 插入到数据库中
    # 方法1
    # student =  Student(name=Student_In.name, pwd=Student_In.pwd, sno=Student_In.sno,clas_id=Student_In.clas_id)
    # await student.save()

    # 方法2
    student = await Student.create(name=Student_In.name, pwd=Student_In.pwd, sno=Student_In.sno,clas_id=Student_In.clas_id)

    # 多对多的对应关系的绑定.
    choose_courses = await Course.filter(id__in=Student_In.courses)
    await student.courses.add(*choose_courses)

    return {
        "操作": "添加一个学生"
    }


@student_api.get("/{student_id}")
async def get_one_student(student_id: int):
    return {
        "操作": f"查看id:{student_id}的一个学生"
    }


@student_api.delete("/{student_id}")
async def delete_student(student_id: int):
    return {
        "操作": f"删除id={student_id}的学生"
    }


@student_api.put("/{student_id}")
async def update_student(student_id: int):
    return {
        "操作": f"更新id={student_id}的学生"
    }
