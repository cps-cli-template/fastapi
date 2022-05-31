# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-05-28 12:09:02.355571
# @Last Modified by: CPS
# @Last Modified time: 2022-05-28 12:09:02.355571
# @file_path "D:\CPS\MyProject\demo\cps-cli\cps-cli-template-fastapi\routers"
# @Filename "upload.py"
# @Description: 试调页面：host:port/file/test
#
import sys
from os import path

sys.path.append("..")
from fastapi import APIRouter, File, UploadFile, Depends, BackgroundTasks
import time

from tools.test import delay

from fastapi.responses import HTMLResponse

from config import get_settings, Settings

router = APIRouter()


async def saveFile(save_path: str, data: bytes) -> bool:
    with open(save_path, "wb") as f:
        f.write(data)
        return True
    return False


# 小文件 bytes类型 以内存方式
@router.post("/file/")
async def create_file(file: bytes = File()):

    return {
        "file_size": len(file),
    }


# 大文件 以io方式
@router.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile, bg: BackgroundTasks, config: Settings = Depends(get_settings)
):

    start = time.time()
    try:
        data = await file.read()
        out_path = path.join(config.upload_path, file.filename)
        res = await saveFile(out_path, data)

        file_info = {
            "success": True,
            "file_name": file.filename,
            "file_content_type": file.content_type,
            "len": len(data),
            "size": f"{round(len(data) / 1024 / 1027, 2)} mb",
            "file_path": out_path,
        }

        # delay(5, msg="处理文件中")
        print("处理开始")
        bg.add_task(delay, 5, msg="处理文件中")
        print("处理完成")
        return file_info
    except Exception as err:
        return {"success": False, "err": err}


# @router.post("/files/")
# async def create_files(files: list[bytes] = File()):
#     return {"file_sizes": [len(file) for file in files]}


# @router.post("/uploadfiles/")
# async def create_upload_files(files: list[UploadFile]):
#     return {"filenames": [file.filename for file in files]}


@router.get("/file/test")
async def main():
    content = """
<style>
form{
    margin: 20px;
    border: 2px solid #C947FF;
    border-radius: 5px;
    padding: 15px;
}
</style>
<body>
<h1>上传接口测试</h1>

<form action="/file/" enctype="multipart/form-data" method="post">
<h2>file/ （小文件）</h2>
<label for="token">Enter your token: </label>
<input type="text" name="token" id="token" required>
<input name="file" type="file">
<input type="submit">
</form>

<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<h2>uploadfile/ （单个大文件）</h2>
<input name="file" type="file">
<input type="submit">
</form>


<form action="/files/" enctype="multipart/form-data" method="post">
<h2>files/</h2>
<input name="files" type="file" multiple>
<input type="submit">
</form>

<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<h2>/uploadfiles/</h2>
<input name="files" type="file" multiple>
<input type="submit">
</form>

</body>
    """
    return HTMLResponse(content=content)
