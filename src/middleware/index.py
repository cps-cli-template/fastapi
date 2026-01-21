# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-10-07 23:10:29.305105
# @Last Modified by: CPS
# @Last Modified time: 2022-10-07 23:10:29.305105
# @file_path "D:\CPS\MyProject\Projects_Personal\YYS\yys-fastapi\src\middleware"
# @Filename "middleware"
# @Description: 通过读取config对应配置，开启预置的中间件
#
import os, sys

sys.path.append("..")

from fastapi import FastAPI

from src.config import Settings
from src.middleware import cors, gzip, http_time, swaggerCache, logger


def init(app: FastAPI, config: Settings) -> FastAPI:
    if config.middleware_gzip_enable:
        gzip.init(app)

    if config.middleware_cors_enable:
        cors.init(app)

    if config.middleware_http_time_count_enable:
        print("---------------------------------------------------3")
        http_time.init(app)

    if config.DEV:
        print("---------------------------------------------------4")
        swaggerCache.init(app)

    logger.init(app)
    return app
