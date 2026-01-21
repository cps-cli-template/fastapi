# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2026-01-19 09:42:39.021476
# @Last Modified by: CPS
# @Last Modified time: 2026-01-19 09:42:39.021476
# @file_path "W:\CPS\MyProject\projsect_persional\cps-cli\cps-cli-template\template-fastapi\src\middleware"
# @Filename "swaggerCache.py"
# @Description: 对swagger的js和css文件进行本地化
#
import os, sys

sys.path.append("..")

from fastapi import FastAPI, Request


def init(app: FastAPI):
    @app.middleware("http")
    async def run(request: Request, call_next):
        path = request.url.path
        print("path: ", path)

        # 如果是swagger静态文件请求.css"]:
        if "/docs" in path:
            print("发现swagger页面请求")

        print("---------------------------------------------------5")
        response = await call_next(request)
        return response

    print("---------------------------------------------------6")

    return app


if __name__ == "__main__":
    pass
