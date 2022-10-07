# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-07-17 17:41:05.028133
# @Last Modified by: CPS
# @Last Modified time: 2022-07-17 17:41:05.028133
# @file_path "D:\CPS\MyProject\Projects_Personal\cps-cli\cps-cli-template-fastapi\events"
# @Filename "startup.py"
# @Description: 功能描述
#
import os, sys

sys.path.append("..")
if __name__ == "__main__":
    sys.path.append("../../")


from os import path
from fastapi import FastAPI

from config import get_settings
from events import config_check
from utils.helper import print_dict


def init(app: FastAPI) -> FastAPI:
    config = get_settings()

    @app.on_event("startup")
    def events_config_check():
        # 检查所有config里面以_path结尾的目录，如果不存在则创建
        config_check.check_path_and_make(config)

    @app.on_event("startup")
    def print_config():
        print_dict(config.dict())
