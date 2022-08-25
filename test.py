# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2022-05-26 20:55:54.506017
# @file_path "D:\CPS\MyProject\外接项目\PSD文件解析\psd-tools"
# @Filename "test.py"
# @Description: 功能描述
#

import uvicorn
from fastapi import FastAPI, Depends

from config import get_settings, Settings
from routers import docs, static, upload
from routers.v1 import test

from middleware import cors, gzip

app = FastAPI(
    title=get_settings().app_name,
    description=get_settings().description,
    version=get_settings().version,
    contact=get_settings().contact,
    docs_url=None,
    redoc_url=None,
    # openapi_url=None,
)


static.init(app, directory="static", route="/static")
docs.init(app, swagger_route="/docs", redoc_route="/redoc")
cors.init(app)
gzip.init(app)

app.include_router(test.router)
app.include_router(upload.router)


@app.get("/", summary="显示当前服务器所有配置（开发模式下）")
async def root(settings: Settings = Depends(get_settings)):
    return {"msg": "当前服务器配置", **settings.dict()}


@app.get("/exit", summary="退出服务器（开发模式下）")
async def Exit():
    exit()


@app.get("/restart", summary="重启服务器（开发模式下）")
async def restart():
    exit()


if __name__ == "__main__":
    from os import path

    file_name = path.splitext(path.basename(__file__))[0]
    uvicorn.run(
        f"{file_name}:app",
        host=get_settings().host,  # 地址
        port=get_settings().port,  # 端口
        log_level=get_settings().log_level,  # 日志等级
        reload=get_settings().DEV,  # 热更新
    )
