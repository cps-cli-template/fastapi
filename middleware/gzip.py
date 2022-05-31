# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-05-28 12:09:02.355571
# @Last Modified by: CPS
# @Last Modified time: 2022-05-28 12:09:02.355571
# @file_path "D:\CPS\MyProject\demo\cps-cli\cps-cli-template-fastapi\middleware"
# @Filename "gzip.py"
# @Description: 功能描述
#

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware


def init(app: FastAPI) -> FastAPI:
    # 不要 GZip 响应小于此最小字节大小。默认为500.
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    return app
