# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-05-28 11:43:09.419969
# @Last Modified by: CPS
# @Last Modified time: 2022-05-28 11:43:09.419969
# @file_path "D:\CPS\MyProject\demo\cps-cli\cps-cli-template-fastapi\middleware"
# @Filename "cors.py"
# @Description: 功能描述
#

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*",
]


def init(app: FastAPI) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_origin_regex=r"^http.*://(localhost|127.0.0.1):\d+$",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
