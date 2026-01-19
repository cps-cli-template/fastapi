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

from os import path
from pathlib import Path
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.base import BaseHTTPMiddleware


class SimpleSwaggerLocalMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.static_dir = Path("static/docs")
        self.static_dir.mkdir(parents=True, exist_ok=True)


def init(app: FastAPI):
    app.add_middleware()


if __name__ == "__main__":
    pass
