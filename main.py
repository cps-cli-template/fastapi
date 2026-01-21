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
from fastapi import FastAPI, Depends

from src.events import onStartup
from src.config import get_settings, Settings

from src.middleware import index as middleware
from src.routers import docs, static, upload, router_template


# 启动事件
config = get_settings()
onStartup.init(config)

app = FastAPI(
    title=config.app_name,
    description=config.app_description,
    version=config.app_version,
    contact=config.app_contact,
    docs_url=None,
    redoc_url=None,
)

upload.init(app)

# 中间件
middleware.init(app, config)

# logger.init(app)
static.init(app)
docs.init(app)

if config.DEV:
    app.include_router(router_template.router)

    @app.get("/", summary="显示当前服务器所有配置 （开发模式下）")
    async def root(settings: Settings = Depends(get_settings)):
        return {"msg": "当前服务器配置", **settings.dict()}

    @app.get("/exit", summary="退出服务器 （开发模式下）")
    async def Exit():
        exit()

    @app.get("/restart", summary="重启服务器 （开发模式下）")
    async def restart():
        exit()


if __name__ == "__main__":
    from os import path
    import sys

    file_name = path.splitext(path.basename(__file__))[0]

    if_frozen = getattr(sys, "frozen", False)
    print("if_frozen: ", if_frozen)

    if if_frozen == False:
        app_inst = f"{file_name}:app"  # 打包后可能启动失败，因为没有py文件了

        reload_flag = config.DEV
    else:
        app_inst = app
        reload_flag = False

    uvicorn.run(
        app=app_inst,
        host=config.app_host,  # 地址
        port=config.app_port,  # 端口
        log_level=config.log_level,  # 日志等级
        reload=reload_flag,  # 热更新
    )
    print(f"app 运行成功，请访问: http://{config.app_host}:{config.app_port}")
