# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-10-07 23:02:54.024122
# @Last Modified by: CPS
# @Last Modified time: 2022-10-07 23:02:54.024122
# @file_path "D:\CPS\MyProject\Projects_Personal\YYS\yys-fastapi\src\middleware"
# @Filename "http_time.py"
# @Description: 功能描述
#
import os, sys, time

sys.path.append("..")

from fastapi import FastAPI, Request


def init(app: FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        """
        计算请求从到达服务器到处理完成的时间
        """
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = f"{str(round(process_time, 3))} ms"
        return response
