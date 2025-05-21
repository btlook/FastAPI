import os.path
from typing import List

from fastapi import APIRouter, UploadFile, File

app05 = APIRouter()


@app05.post("/file")
# async def get_file(file: bytes = File()):
async def get_file(file: UploadFile = File()):
    print("file", file)

    path = os.path.join("imgs", file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())

    return {
        "file": file.filename,
    }


@app05.post("/files")
# async def get_file(file: bytes = File()):
async def get_files(files: List[UploadFile] = File()):
    print("file", files)

    return {
        "file": len(files)
    }
