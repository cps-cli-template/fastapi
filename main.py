# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2022-05-26 20:55:54.506017
# @file_path "D:\CPS\MyProject\外接项目\PSD文件解析\psd-tools"
# @Filename "app.py"
# @Description: 功能描述
#

import uvicorn

from fastapi import FastAPI
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)


from config import Settings, contact, get_settings

from routers import docs
from routers.v1 import test


app = FastAPI(
    title=get_settings().app_name,
    description=get_settings().description,
    version=get_settings().version,
    contact=contact,
    docs_url=None,
    redoc_url=None,
    # openapi_url=None,
)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(test.router)
app.include_router(docs.init(app))


@app.get("/", summary="显示当前服务器所有配置 （开发模式下）")
async def root(settings: Settings = Depends(get_settings)):
    return {"msg": "当前服务器配置", **settings.dict()}


@app.get("/exit", summary="退出服务器 （开发模式下）")
async def Exit():
    exit()


@app.get("/restart", summary="重启服务器 （开发模式下）")
async def restart():
    exit()


def run():
    uvicorn.run(
        "main:app",
        host=get_settings().host,  # 地址
        port=get_settings().port,  # 端口
        log_level=get_settings().log_level,  # 日志等级
        reload=get_settings().DEV,  # 热更新
    )


if __name__ == "__main__":
    run()
