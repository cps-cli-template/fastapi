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
from fastapi import APIRouter, File, UploadFile, Depends, BackgroundTasks, HTTPException
import time

from tools.test import delay
from tools.uploader import Uploader
from fastapi.responses import HTMLResponse
from config import get_settings, Settings
from Types import Res, Err, Fileinfo

router = APIRouter()


@router.post("/upload")
async def create_upload_file(
    file: File(...), bg: BackgroundTasks, config: Settings = Depends(get_settings)
):
    output_path = path(config.path_upload, file.filename)

    upload_res = await Uploader.stream_file(file, output_path)

    if upload_res:
        return Res(msg="上传成功")
    else:
        raise HTTPException(detail="上传失败")


# 大文件(单个)
# 大文件(多个)
# 小文件(单个)
# 小文件(多个)

# 小文件 以io方式
@router.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile, bg: BackgroundTasks, config: Settings = Depends(get_settings)
):
    try:
        data = await file.read()
        out_path = path.join(config.upload_path, file.filename)
        has_upload = await Uploader.small_file(out_path, data)

        size = f"{round(len(data) / 1024 / 1027, 2)} mb"
        file_info = Fileinfo(
            len=len(data),
            size=size,
            file_name=file.filename,
            file_type=file.content_type,
            file_path=out_path,
        )

        # delay(5, msg="处理文件中")
        bg.add_task(delay, 5, msg="处理文件中")

        if has_upload:
            return Res(msg="上传成功", res=file_info)

        return Err(msg="上传失败")
    except Exception as err:
        return {"success": False, "err": err}


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

</body>"""

    return HTMLResponse(content=content)
